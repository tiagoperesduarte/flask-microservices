from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from app.exceptions.http_exceptions import ResourceNotFoundException
from app.models.product import Product
from app.resources.schemas.product_schema import ProductQueryArgsSchema, ProductResponseSchema, ProductRequestSchema
from app.services.product_service import ProductService

product_blp = Blueprint(
    'products', 'products', url_prefix='/api/products'
)

product_service = ProductService()


@product_blp.route('', methods=['GET'])
@product_blp.arguments(ProductQueryArgsSchema, location='query')
@product_blp.response(ProductResponseSchema(many=True))
@jwt_required
def get_products(args):
    name = args.get('name')
    page = args.get('page', 1)
    per_page = args.get('per_page', 10)

    return product_service.get_products(name, page, per_page)


@product_blp.route('/<product_id>', methods=['GET'])
@product_blp.response(ProductResponseSchema)
@jwt_required
def get_product_by_id(product_id):
    try:
        return product_service.get_product_by_id(product_id)
    except ResourceNotFoundException as e:
        abort(404, message=str(e))


@product_blp.route('', methods=['POST'])
@product_blp.arguments(ProductRequestSchema)
@product_blp.response(ProductResponseSchema, code=201)
@jwt_required
def create_product(data):
    product = Product.from_dict(data)
    return product_service.create_product(product)


@product_blp.route('/<product_id>', methods=['PUT'])
@product_blp.arguments(ProductRequestSchema)
@product_blp.response(ProductResponseSchema)
@jwt_required
def update_product(data, product_id):
    try:
        product = Product.from_dict(data)
        return product_service.update_product(product_id, product)
    except ResourceNotFoundException as e:
        abort(404, message=str(e))


@product_blp.route('/<product_id>', methods=['DELETE'])
@product_blp.response(code=204)
@jwt_required
def delete_product_by_id(product_id):
    try:
        product_service.delete_product_by_id(product_id)
    except ResourceNotFoundException as e:
        abort(404, message=str(e))
