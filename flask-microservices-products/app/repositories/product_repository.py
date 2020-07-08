from flask_mongoengine import Pagination
from mongoengine import DoesNotExist

from app.models.product import Product


class ProductRepository:
    def get_products(self, name, page, per_page):
        products = []

        if not name:
            products = Product.objects()
        else:
            products = Product.objects(name__contains=name)

        return Pagination(products, page, per_page).items

    def get_product_by_id(self, id):
        try:
            return Product.objects.get(id=id)
        except DoesNotExist as err:
            return None

    def product_exists_by_id(self, id):
        product = self.get_product_by_id(id)

        if not product:
            return False

        return True

    def save_product(self, product):
        return product.save()

    def delete_product_by_id(self, id):
        Product.objects.get(id=id).delete()
