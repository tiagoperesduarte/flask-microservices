from flask import Flask

from app.configs.database_config import configure_db
from app.configs.routes_config import configure_routes
from app.configs.security_config import configure_security


def create_app():
    app = Flask(__name__)

    configure_db(app)
    configure_security(app)
    configure_routes(app)

    return app
