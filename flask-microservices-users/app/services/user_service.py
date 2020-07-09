from app.errors.resource_not_found_error import ResourceNotFoundError
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self, name, page, per_page):
        return self.user_repository.get_users(name, page, per_page)

    def get_user_by_id(self, id):
        user = self.user_repository.get_user_by_id(id)

        if not user:
            raise ResourceNotFoundError(f'User not found with identifier {id}')

        return self.user_repository.get_user_by_id(id)

    def user_exists_by_id(self, id):
        return self.user_repository.user_exists_by_id(id)

    def create_user(self, user):
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
