import pytest
from flask_pytest_intro import app

@pytest.fixture
def flask_app():
    yield app.app

@pytest.fixture
def client(flask_app):
    """A test client for the app."""
    return flask_app.test_client()
