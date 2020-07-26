from flask_jwt_extended import get_raw_jwt

from app.security.current_user import CurrentUser


class SecurityUtils:
    @classmethod
    def get_current_user(cls):
        token = get_raw_jwt()

        if not token:
            return None

        return CurrentUser.from_token(token)
