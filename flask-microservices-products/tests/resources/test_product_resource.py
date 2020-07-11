import pytest

from app.models.product import Product
from tests.mock.product_mock import get_mock_product

API_URL = '/api/products'


@pytest.fixture(autouse=True)
def cleanup():
    Product.drop_collection()


def test_product_list_all(client):
    number_products = 3

    for i in range(number_products):
        client.post(API_URL, json=get_mock_product())

    res = client.get(API_URL)
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == number_products


def test_product_list_empty(client):
    res = client.get(API_URL)
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == 0


def test_product_list_pagination_per_page(client):
    per_page = 5
    number_products = per_page + 1

    for i in range(number_products):
        client.post(API_URL, json=get_mock_product())

    res = client.get(f'{API_URL}?per_page={per_page}')
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == per_page


def test_product_list_by_name(client):
    mock_products = [
        get_mock_product(name='Smart TV LED 49LH5600 LG'),
        get_mock_product(name='Micro-ondas Philco 25 Litros Cinza'),
        get_mock_product(name='Soundbar LG SK9Y')
    ]

    keyword = mock_products[0]['name']

    for mock_product in mock_products:
        client.post(API_URL, json=mock_product)

    res = client.get(f'{API_URL}?name={keyword}')
    data = res.json

    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert len(data) == 1
    assert data[0]['name'] == keyword


def test_product_create_success(client):
    res = client.post(API_URL, json=get_mock_product())

    assert res.status_code == 201
    assert res.content_type == 'application/json'


def test_product_create_bad_request(client):
    res = client.post(API_URL, json={})

    assert res.status_code == 422
    assert res.content_type == 'application/json'


def test_product_delete_success(client):
    res_post = client.post(API_URL, json=get_mock_product())
    product_id = res_post.json['id']

    res_delete = client.delete(f'{API_URL}/{product_id}')

    assert res_delete.status_code == 204
    assert res_delete.content_type == 'application/json'


def test_product_delete_not_found(client):
    product_id = 123456
    res = client.delete(f'{API_URL}/{product_id}')

    assert res.status_code == 404
    assert res.content_type == 'application/json'
