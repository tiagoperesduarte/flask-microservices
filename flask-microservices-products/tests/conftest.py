import pytest

from app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True

    return app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
