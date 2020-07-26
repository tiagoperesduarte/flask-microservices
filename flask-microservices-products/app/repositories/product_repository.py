from flask_mongoengine import Pagination
from mongoengine import DoesNotExist, ValidationError

from app.models.product import Product


class ProductRepository:
    def get_products_by_user_id(self, user_id, name, page, per_page):
        products = []

        if not name:
            products = Product.objects(user_id=user_id)
        else:
            products = Product.objects(user_id=user_id, name__icontains=name)

        return Pagination(products, page, per_page).items

    def get_product_by_id_and_user_id(self, id, user_id):
        try:
            return Product.objects.get(id=id, user_id=user_id)
        except DoesNotExist:
            return None
        except ValidationError:
            return None

    def product_exists_by_id_and_user_id(self, id, user_id):
        product = self.get_product_by_id_and_user_id(id, user_id)

        if not product:
            return False

        return True

    def save_product(self, product):
        return product.save()

    def delete_product_by_id_and_user_id(self, id, user_id):
        Product.objects.get(id=id, user_id=user_id).delete()
