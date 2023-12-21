import pytest


def test_users_case1(client):
    response = client.post("/users", json={"fullName": "Alice Norton"})
    assert response.status_code == 200
    pass


def test_users_case2(client):
    response = client.post("/users", json={"fullname": "Alice Norton"})
    assert response.status_code == 400
    pass
