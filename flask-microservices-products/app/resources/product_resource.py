from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.models.product import Product
from app.schemas.product_schema import ProductRequestSchema, ProductResponseSchema, ProductQueryArgsSchema
from app.services.product_service import ProductService

product_blp = Blueprint(
    'products', 'products', url_prefix='/api/products'
)

product_service = ProductService()


@product_blp.route('', methods=['GET'])
@product_blp.arguments(ProductQueryArgsSchema, location='query')
@product_blp.response(ProductResponseSchema(many=True))
def get_products(args):
    name = args.get('name')
    page = args.get('page', 1)
    per_page = args.get('per_page', 10)

    return product_service.get_products(name, page, per_page)


@product_blp.route('/<product_id>', methods=['GET'])
@product_blp.response(ProductResponseSchema)
def get_product_by_id(product_id):
    try:
        return product_service.get_product_by_id(product_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@product_blp.route('', methods=['POST'])
@product_blp.arguments(ProductRequestSchema)
@product_blp.response(ProductResponseSchema, code=201)
def create_product(data):
    product = Product.from_dict(data)
    return product_service.create_product(product)


@product_blp.route('/<product_id>', methods=['PUT'])
@product_blp.arguments(ProductRequestSchema)
@product_blp.response(ProductResponseSchema)
def update_product(data, product_id):
    try:
        product = Product.from_dict(data)
        return product_service.update_product(product_id, product)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@product_blp.route('/<product_id>', methods=['DELETE'])
@product_blp.response(code=204)
def delete_product_by_id(product_id):
    try:
        product_service.delete_product_by_id(product_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))
