from flask import Flask

from app.config.database import configure_db
from app.config.routes import configure_routes


def create_app():
    app = Flask(__name__)

    configure_db(app)
    configure_routes(app)

    return app
