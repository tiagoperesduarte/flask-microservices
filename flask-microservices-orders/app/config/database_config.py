from flask_mongoengine import MongoEngine

from app.utils.env_utils import EnvUtils

db = MongoEngine()


def configure_db(app):
    app.config['MONGODB_HOST'] = EnvUtils.get_env('APP_DB_URI')
    app.config['MONGODB_USERNAME'] = EnvUtils.get_env('APP_DB_USERNAME')
    app.config['MONGODB_PASSWORD'] = EnvUtils.get_env('APP_DB_PASSWORD')

    db.init_app(app)
