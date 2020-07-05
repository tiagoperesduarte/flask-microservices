from flask_restful import Resource, reqparse

from app.models.product import Product
from app.services.product_service import ProductService

product_service = ProductService()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('description', type=str, required=True)
parser.add_argument('price', type=float, required=True)


class ProductResource(Resource):
    def get(self, id):
        product = product_service.get_product_by_id(id)

        if not product:
            return {'message': f'Product not found with identifier {id}'}, 404

        return product.to_dict()

    def put(self, id):
        product = product_service.get_product_by_id(id)

        if not product:
            return {'message': f'Product not found with identifier {id}'}, 404

        data = parser.parse_args()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']

        saved_product = product_service.save_product(product)

        return saved_product.to_dict()

    def delete(self, id):
        product = product_service.get_product_by_id(id)

        if not product:
            return {'message': f'Product not found with identifier {id}'}, 404

        product_service.delete_product_by_id(id)


class ProductListResource(Resource):
    def get(self):
        return [product.to_dict() for product in product_service.get_products()]

    def post(self):
        data = parser.parse_args()
        saved_product = product_service.save_product(Product.from_dict(data))

        return saved_product.to_dict(), 201
