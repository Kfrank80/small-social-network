import pytest
from main import app as _app


@pytest.fixture()
def app():
    app = _app
    app.app.config.update({
        "TESTING": True,
    })


@pytest.fixture()
def client(app):
    return _app.test_client()


@pytest.fixture()
def runner(app):
    return _app.test_cli_runner()
