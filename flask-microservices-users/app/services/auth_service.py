from app.errors.bad_credentials_error import BadCredentialsError
from app.models.current_user import CurrentUser
from app.repositories.user_repository import UserRepository
from app.utils.security_utils import SecurityUtils


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate(self, email, password):
        user = self.user_repository.get_user_by_email(email)

        if not user or not user.verify_password(password):
            raise BadCredentialsError('Email or password incorrect')

        return CurrentUser.from_user(user)

    def create_token(self, email, password):
        current_user = self.authenticate(email, password)

        return {
            'access_token': SecurityUtils.create_access_token(current_user),
            'refresh_token': SecurityUtils.create_refresh_token(current_user)
        }

    def refresh_token(self):
        current_user = SecurityUtils.get_current_user()

        return {
            'access_token': SecurityUtils.create_access_token(current_user),
            'refresh_token': SecurityUtils.create_refresh_token(current_user)
        }
