import datetime

from flask_jwt_extended import JWTManager

from app.utils.env_utils import EnvUtils

jwt = JWTManager()


def configure_security(app):
    access_token_expires = datetime.timedelta(seconds=int(EnvUtils.get_env('APP_SECURITY_ACCESS_TOKEN_EXPIRES')))
    refresh_token_expires = datetime.timedelta(seconds=int(EnvUtils.get_env('APP_SECURITY_REFRESH_TOKEN_EXPIRES')))

    app.config['JWT_SECRET_KEY'] = EnvUtils.get_env('APP_SECURITY_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = access_token_expires
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = refresh_token_expires

    jwt.init_app(app)


@jwt.user_identity_loader
def user_identity_lookup(current_user):
    return str(current_user.id)
