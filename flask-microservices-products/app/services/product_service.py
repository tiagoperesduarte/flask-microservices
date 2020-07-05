from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_products(self):
        return self.product_repository.get_products()

    def get_product_by_id(self, id):
        return self.product_repository.get_product_by_id(id)

    def save_product(self, product):
        return self.product_repository.save_product(product)

    def delete_product_by_id(self, id):
        self.product_repository.delete_product_by_id(id)
