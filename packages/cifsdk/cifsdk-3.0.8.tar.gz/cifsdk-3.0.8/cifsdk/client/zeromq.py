import time
import json
from cifsdk.client import Client
from cifsdk.msg import Msg
from cifsdk.exceptions import AuthError, CIFConnectionError, TimeoutError, InvalidSearch, CIFBusy
from cifsdk.constants import PYVERSION
from csirtg_indicator import Indicator
import logging
import os
import zlib
from zmq.eventloop.ioloop import IOLoop
from pprint import pprint

import zmq

SNDTIMEO = os.environ.get('ZMQ_SNDTIMEO', 90000)  # 90s
RCVTIMEO = os.environ.get('ZMQ_RCVTIMEO', 90000)  # 90s
LINGER = 3
ENCODING_DEFAULT = "utf-8"
SEARCH_LIMIT = 100
FIREBALL_SIZE = os.getenv('CIFSDK_CLIENT_ZEROMQ_FIREBALL_SIZE', 500)
FIREBALL_SIZE = int(FIREBALL_SIZE)

logger = logging.getLogger(__name__)

TRACE = os.getenv('CIFSDK_CLIENT_ZEROMQ_TRACE') or os.getenv('CIFSDK_CLIENT_ZMQ_TRACE')

logger = logging.getLogger(__name__)

logger.setLevel(logging.ERROR)

if TRACE:
    logger.setLevel(logging.DEBUG)

if PYVERSION == 3:
    basestring = (str, bytes)


class ZMQ(Client):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        self.context.term()

    def __init__(self, remote, token, **kwargs):
        super(ZMQ, self).__init__(remote, token)

        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.RCVTIMEO = RCVTIMEO
        self.socket.SNDTIMEO = SNDTIMEO
        self.socket.setsockopt(zmq.LINGER, LINGER)
        self.autoclose = kwargs.get('autoclose', True)
        self.nowait = kwargs.get('nowait', False)
        if self.nowait:
            self.socket = self.context.socket(zmq.DEALER)

    def _recv(self, decode=True):
        mtype, data = Msg().recv(self.socket)

        if not decode:
            return data

        data = json.loads(data)

        if data.get('message') == 'unauthorized':
            raise AuthError()

        if data.get('message') == 'busy':
            raise CIFBusy()

        if data.get('message') == 'invalid search':
            raise InvalidSearch()

        if data.get('status') != 'success':
            raise RuntimeError(data.get('message'))

        if data.get('data') is None:
            raise RuntimeError('invalid response')

        if isinstance(data.get('data'), bool):
            return data['data']

        # is this a straight up elasticsearch string?
        if data['data'] == '{}':
            return []

        if isinstance(data['data'], basestring) and data['data'].startswith('{"hits":{"hits":[{"_source":'):
            data['data'] = json.loads(data['data'])
            data['data'] = [r['_source'] for r in data['data']['hits']['hits']]

        try:
            data['data'] = zlib.decompress(data['data'])
        except (zlib.error, TypeError):
            pass

        return data.get('data')

    def _send(self, mtype, data='[]', nowait=False, decode=True):

        self.socket.connect(self.remote)

        if isinstance(data, str):
            data = data.encode('utf-8')

        Msg(mtype=mtype, token=self.token, data=data).send(self.socket)

        if self.nowait or nowait:
            if self.autoclose:
                self.socket.close()
            logger.debug('not waiting for a resp')
            return

        rv = self._recv(decode=decode)
        self.socket.close()
        return rv

    def ping(self, write=False):
        if write:
            return self._send(Msg.PING_WRITE)

        return self._send(Msg.PING)

    def tokens_search(self, filters={}):
        return self._send(Msg.TOKENS_SEARCH, json.dumps(filters))

    def tokens_create(self, data):
        return self._send(Msg.TOKENS_CREATE, data)

    def tokens_delete(self, data):
        return self._send(Msg.TOKENS_DELETE, data)

    def tokens_edit(self, data):
        return self._send(Msg.TOKENS_EDIT, data)

    def _handle_message_fireball(self, s, e):
        logger.debug('message received')

        id, mtype, data = Msg().recv(s)

        self.response.append(data)

        self.num_responses -= 1
        logger.debug('num responses remaining: %i' % self.num_responses)

        if self.num_responses == 0:
            logger.debug('finishing up...')
            self.loop.stop()

    def _fireball_timeout(self):
        logger.warn('timeout')
        self.loop.stop()
        raise TimeoutError('timeout')

    def _send_fireball(self, mtype, data):
        if len(data) < 3:
            logger.error('no data to send')
            return []

        self.loop = IOLoop()
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.connect(self.remote)

        timeout = time.time() + SNDTIMEO
        self.loop.add_timeout(timeout, self._fireball_timeout)
        self.response = []

        self.loop.add_handler(self.socket, self._handle_message_fireball, zmq.POLLIN)

        if PYVERSION == 3:
            if isinstance(data, bytes):
                data = data.decode('utf-8')

        data = json.loads(data)

        if not isinstance(data, list):
            data = [data]

        if (len(data) % FIREBALL_SIZE) == 0:
            self.num_responses = int((len(data) / FIREBALL_SIZE))
        else:
            self.num_responses = int((len(data) / FIREBALL_SIZE)) + 1

        logger.debug('responses expected: %i' % self.num_responses)

        batch = []
        for d in data:
            batch.append(d)
            if len(batch) == FIREBALL_SIZE:
                Msg(mtype=Msg.INDICATORS_CREATE, token=self.token, data=batch).send(self.socket)
                batch = []

        if len(batch):
            Msg(mtype=Msg.INDICATORS_CREATE, token=self.token, data=batch).send(self.socket)

        logger.debug("starting loop to receive")
        self.loop.start()
        self.loop.close()
        self.socket.close()
        return self.response

    def indicators_search(self, filters, decode=True):
        return self._send(Msg.INDICATORS_SEARCH, json.dumps(filters), decode=decode)

    def indicators_create(self, data, nowait=False, fireball=False):
        if isinstance(data, dict):
            data = self._kv_to_indicator(data)

        if isinstance(data, Indicator):
            data = str(data)

        if fireball:
            logger.info('using fireball mode')
            return self._send_fireball(Msg.INDICATORS_CREATE, data)

        return self._send(Msg.INDICATORS_CREATE, data, nowait=nowait)

    def indicators_delete(self, data):
        if isinstance(data, dict):
            data = self._kv_to_indicator(data)

        if isinstance(data, Indicator):
            data = str(data)

        return self._send(Msg.INDICATORS_DELETE, data)

Plugin = ZMQ
