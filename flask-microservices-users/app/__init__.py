from flask import Flask

from app.config.bcrypt_config import configure_bcrypt
from app.config.database_config import configure_db
from app.config.routes_config import configure_routes
from app.config.security_config import configure_security


def create_app():
    app = Flask(__name__)

    configure_security(app)
    configure_bcrypt(app)
    configure_db(app)
    configure_routes(app)

    return app
