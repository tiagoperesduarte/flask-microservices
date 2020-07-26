from app.errors.resource_not_found_error import ResourceNotFoundError
from app.errors.user_already_exists_error import UserAlreadyExistsError
from app.repositories.user_repository import UserRepository
from app.security.security_utils import SecurityUtils


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self, name, page, per_page):
        return self.user_repository.get_users(name, page, per_page)

    def get_current_user(self):
        current_user = SecurityUtils.get_current_user()
        return self.get_user_by_id(current_user.id)

    def get_user_by_id(self, id):
        user = self.user_repository.get_user_by_id(id)

        if not user:
            raise ResourceNotFoundError(f'User not found with identifier {id}')

        return user

    def get_user_by_email(self, email):
        user = self.user_repository.get_user_by_email(email)

        if not user:
            raise ResourceNotFoundError(f'User not found with identifier {email}')

        return user

    def user_exists_by_id(self, id):
        return self.user_repository.user_exists_by_id(id)

    def user_exists_by_email(self, email):
        return self.user_repository.user_exists_by_email(email)

    def create_user(self, user):
        exists = self.user_exists_by_email(user.email)

        if exists:
            raise UserAlreadyExistsError('That email address is already in use')

        user.id = None
        user.hash_password()

        return self.user_repository.save_user(user)

    def update_user(self, id, user):
        if not self.user_exists_by_id(id):
            raise ResourceNotFoundError(f'User not found with identifier {id}')

        user.id = id

        return self.user_repository.save_user(user)

    def delete_user_by_id(self, id):
        user = self.user_repository.get_user_by_id(id)

        if not user:
            raise ResourceNotFoundError(f'User not found with identifier {id}')

        self.user_repository.delete_user_by_id(id)
