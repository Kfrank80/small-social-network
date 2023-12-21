import pytest


def test_user_wall(client):
    response = client.get("/walls/1")
    assert response.status_code == 200
    pass


def test_add_like(client):
    response = client.post("/users/1/liked/2", data="")
    assert response.status_code == 200
    pass


def test_dislike(client):
    response = client.post("/users/1/disliked/2", data="")
    assert response.status_code == 200
    pass
