from mongoengine import DoesNotExist

from app.models.product import Product


class ProductRepository:
    def get_products(self):
        return Product.objects

    def get_product_by_id(self, id):
        try:
            return Product.objects.get(id=id)
        except DoesNotExist as err:
            return None

    def save_product(self, product):
        return product.save()

    def delete_product_by_id(self, id):
        Product.objects.get(id=id).delete()
