from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.models.product import Product
from app.schemas.product_schema import ProductSchema
from app.services.product_service import ProductService

blp = Blueprint(
    'products', 'products', url_prefix='/api/products'
)

product_service = ProductService()


@blp.route('')
class Products(MethodView):
    @blp.response(ProductSchema(many=True))
    def get(self):
        return product_service.get_products()

    @blp.arguments(ProductSchema)
    @blp.response(ProductSchema, code=201)
    def post(self, data):
        product = Product.from_dict(data)
        return product_service.create_product(product)


@blp.route('/<product_id>')
class ProductsById(MethodView):
    @blp.response(ProductSchema)
    def get(self, product_id):
        try:
            return product_service.get_product_by_id(product_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @blp.arguments(ProductSchema)
    @blp.response(ProductSchema)
    def put(self, data, product_id):
        try:
            product = Product.from_dict(data)
            return product_service.update_product(product_id, product)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))

    @blp.response(code=204)
    def delete(self, product_id):
        try:
            product_service.delete_product_by_id(product_id)
        except ResourceNotFoundError as e:
            abort(404, message=str(e))
