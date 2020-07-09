from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.models.user import User
from app.schemas.user_schema import UserRequestSchema, UserResponseSchema, UserQueryArgsSchema
from app.services.user_service import UserService

user_blp = Blueprint(
    'users', 'users', url_prefix='/api/users'
)

user_service = UserService()


@user_blp.route('')
class Users(MethodView):
    @user_blp.arguments(UserQueryArgsSchema, location='query')
    @user_blp.response(UserResponseSchema(many=True))
    def get(self, args):
        name = args.get('name')
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        return user_service.get_users(name, page, per_page)

    @user_blp.arguments(UserRequestSchema)
    @user_blp.response(UserResponseSchema, code=201)
    def post(self, data):
        user = User.from_dict(data)
        return user_service.create_user(user)


@user_blp.route('/<user_id>')
class UsersById(MethodView):
    @user_blp.response(UserResponseSchema)
    def get(self, user_id):
        try:
            return user_service.get_user_by_id(user_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @user_blp.arguments(UserRequestSchema)
    @user_blp.response(UserResponseSchema)
    def put(self, data, user_id):
        try:
            user = User.from_dict(data)
            return user_service.update_user(user_id, user)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @user_blp.response(code=204)
    def delete(self, user_id):
        try:
            user_service.delete_user_by_id(user_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))
