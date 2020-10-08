from flask_jwt_extended import jwt_refresh_token_required
from flask_smorest import Blueprint, abort

from app.errors.bad_credentials_error import BadCredentialsError
from app.resources.schemas.auth_schema import AuthRequestSchema, AuthResponseSchema
from app.services.auth_service import AuthService

auth_blp = Blueprint(
    'auth', 'auth', url_prefix='/api/auth'
)

auth_service = AuthService()


@auth_blp.route('/login', methods=['POST'])
@auth_blp.arguments(AuthRequestSchema)
@auth_blp.response(AuthResponseSchema, code=200)
def login(data):
    try:
        return auth_service.authenticate(data['email'], data['password'])
    except BadCredentialsError as e:
        abort(401, message=str(e))


@auth_blp.route('/refresh', methods=['POST'])
@auth_blp.response(AuthResponseSchema, code=200)
@jwt_refresh_token_required
def refresh_token():
    return auth_service.refresh_token()
