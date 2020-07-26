import pytest
from flask_jwt_extended import create_access_token

from app import create_app
from app.models.current_user import CurrentUser


@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True

    return app


@pytest.fixture(scope='session')
def client(app):
    with app.app_context():
        access_token = create_access_token(identity=CurrentUser(id="123456"), expires_delta=False)

        client = app.test_client()
        client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'

        return client
