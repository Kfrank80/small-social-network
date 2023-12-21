import pytest


def test_add_post(client):
    response = client.post("/posts", json={
        "userId": 3,
        "text": "Hello world!",
        "visibility": "private"
    })
    assert response.status_code == 200
    pass

