import pytest


def test_add_friendship(client):
    response = client.post("/users/1/friends/3", data="")
    assert response.status_code == 200
    pass


def test_add_follower(client):
    response = client.post("/users/2/followers/3", data="")
    assert response.status_code == 200
    pass
