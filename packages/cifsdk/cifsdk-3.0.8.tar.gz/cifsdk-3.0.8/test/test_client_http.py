import py.test

from cifsdk.client.http import HTTP as Client


def test_client_http():
    cli = Client('https://localhost:3000', '12345')
    assert cli.remote == 'https://localhost:3000'

    assert cli.token == '12345'
