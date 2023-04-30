from hello import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!\n'
