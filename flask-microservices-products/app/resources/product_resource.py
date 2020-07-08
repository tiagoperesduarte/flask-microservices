from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.models.product import Product
from app.schemas.product_schema import ProductRequestSchema, ProductResponseSchema, ProductQueryArgsSchema
from app.services.product_service import ProductService

product_blp = Blueprint(
    'products', 'products', url_prefix='/api/products'
)

product_service = ProductService()


@product_blp.route('')
class Products(MethodView):
    @product_blp.arguments(ProductQueryArgsSchema, location='query')
    @product_blp.response(ProductResponseSchema(many=True))
    def get(self, args):
        name = args.get('name')
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        return product_service.get_products(name, page, per_page)

    @product_blp.arguments(ProductRequestSchema)
    @product_blp.response(ProductResponseSchema, code=201)
    def post(self, data):
        product = Product.from_dict(data)
        return product_service.create_product(product)


@product_blp.route('/<product_id>')
class ProductsById(MethodView):
    @product_blp.response(ProductResponseSchema)
    def get(self, product_id):
        try:
            return product_service.get_product_by_id(product_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @product_blp.arguments(ProductRequestSchema)
    @product_blp.response(ProductResponseSchema)
    def put(self, data, product_id):
        try:
            product = Product.from_dict(data)
            return product_service.update_product(product_id, product)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @product_blp.response(code=204)
    def delete(self, product_id):
        try:
            product_service.delete_product_by_id(product_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))
