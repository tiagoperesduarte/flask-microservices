import pytest

from app.models.user import User
from app.utils.string_utils import StringUtils
from tests.mock.user_mock import get_mock_user

API_URL = '/api/users'


@pytest.fixture(autouse=True)
def cleanup():
    User.drop_collection()


def test_user_list_all(client):
    number_users = 3

    for i in range(number_users):
        client.post(API_URL, json=get_mock_user())

    res = client.get(API_URL)
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == number_users


def test_user_list_empty(client):
    res = client.get(API_URL)
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == 0


def test_user_list_pagination_per_page(client):
    per_page = 5
    number_users = per_page + 1

    for i in range(number_users):
        client.post(API_URL, json=get_mock_user())

    res = client.get(f'{API_URL}?per_page={per_page}')
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == per_page


def test_user_list_by_name(client):
    mock_users = [
        get_mock_user(name='Lucas Ribeiro Silva'),
        get_mock_user(name='Pedro Henrique Barroso'),
        get_mock_user(name='Enaldo Rocha Cardoso')
    ]

    wanted_user = mock_users[0]
    keyword = StringUtils.get_first_word(wanted_user['name'])

    for mock_user in mock_users:
        client.post(API_URL, json=mock_user)

    res = client.get(f'{API_URL}?name={keyword}')
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == 1
    assert data[0]['name'] == wanted_user['name']


def test_user_create_success(client):
    res = client.post(API_URL, json=get_mock_user())

    assert res.status_code == 201
    assert res.content_type == 'application/json'


def test_user_create_bad_request(client):
    res = client.post(API_URL, json={})

    assert res.status_code == 422
    assert res.content_type == 'application/json'


def test_user_delete_success(client):
    res_post = client.post(API_URL, json=get_mock_user())
    user_id = res_post.json['id']

    res_delete = client.delete(f'{API_URL}/{user_id}')

    assert res_delete.status_code == 204
    assert res_delete.content_type == 'application/json'


def test_user_delete_not_found(client):
    user_id = 123456
    res = client.delete(f'{API_URL}/{user_id}')

    assert res.status_code == 404
    assert res.content_type == 'application/json'
