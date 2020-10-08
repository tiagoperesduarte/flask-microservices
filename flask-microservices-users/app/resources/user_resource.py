from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.errors.user_already_exists_error import UserAlreadyExistsError
from app.models.user import User
from app.resources.schemas.user_schema import UserQueryArgsSchema, UserResponseSchema, UserRequestSchema
from app.services.user_service import UserService

user_blp = Blueprint(
    'users', 'users', url_prefix='/api/users'
)

user_service = UserService()


@user_blp.route('', methods=['GET'])
@user_blp.arguments(UserQueryArgsSchema, location='query')
@user_blp.response(UserResponseSchema(many=True))
@jwt_required
def get_users(args):
    name = args.get('name')
    page = args.get('page', 1)
    per_page = args.get('per_page', 10)

    return user_service.get_users(name, page, per_page)


@user_blp.route('/<user_id>', methods=['GET'])
@user_blp.response(UserResponseSchema)
@jwt_required
def get_user_by_id(user_id):
    try:
        return user_service.get_user_by_id(user_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@user_blp.route('/me', methods=['GET'])
@user_blp.response(UserResponseSchema)
@jwt_required
def get_current_user():
    try:
        return user_service.get_current_user()
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@user_blp.route('', methods=['POST'])
@user_blp.arguments(UserRequestSchema)
@user_blp.response(UserResponseSchema, code=201)
def create_user(data):
    try:
        user = User.from_dict(data)
        return user_service.create_user(user)
    except UserAlreadyExistsError as e:
        abort(409, message=str(e))


@user_blp.route('/<user_id>', methods=['PUT'])
@user_blp.arguments(UserRequestSchema)
@user_blp.response(UserResponseSchema)
@jwt_required
def update_user(data, user_id):
    try:
        user = User.from_dict(data)
        return user_service.update_user(user_id, user)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@user_blp.route('/<user_id>', methods=['DELETE'])
@user_blp.response(code=204)
@jwt_required
def delete_user_by_id(user_id):
    try:
        user_service.delete_user_by_id(user_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))
