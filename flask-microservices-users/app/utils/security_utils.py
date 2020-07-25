from flask_jwt_extended import get_raw_jwt, create_access_token, create_refresh_token

from app.models.current_user import CurrentUser


class SecurityUtils:
    @classmethod
    def get_current_user(cls):
        token = get_raw_jwt()

        return CurrentUser.from_token(token)

    @classmethod
    def create_access_token(cls, current_user):
        return create_access_token(identity=current_user)

    @classmethod
    def create_refresh_token(cls, current_user):
        return create_refresh_token(identity=current_user)
