from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def configure_bcrypt(app):
    bcrypt.init_app(app)
