from flask_mongoengine import Pagination
from mongoengine import DoesNotExist

from app.models.user import User


class UserRepository:
    def get_users(self, name, page, per_page):
        users = []

        if not name:
            users = User.objects()
        else:
            users = User.objects(name__contains=name)

        return Pagination(users, page, per_page).items

    def get_user_by_id(self, id):
        try:
            return User.objects.get(id=id)
        except DoesNotExist as err:
            return None

    def user_exists_by_id(self, id):
        user = self.get_user_by_id(id)

        if not user:
            return False

        return True

    def save_user(self, user):
        return user.save()

    def delete_user_by_id(self, id):
        User.objects.get(id=id).delete()
