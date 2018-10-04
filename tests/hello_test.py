def test_hello_pass(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_hello_fail(client):
    response = client.get('/')
    assert response.data == b'Hello, Worlds!'
