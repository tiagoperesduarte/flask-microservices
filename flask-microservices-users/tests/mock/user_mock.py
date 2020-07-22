from app.utils.string_utils import StringUtils


def get_mock_user(name=None, email=None):
    if not name:
        name = f'Usuário {StringUtils.get_random_string()}'

    if not email:
        email = f'{StringUtils.sanitize_string(name)}@email.com'

    return {
        'name': name,
        'email': email
    }
