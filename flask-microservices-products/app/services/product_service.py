from app.errors.resource_not_found_error import ResourceNotFoundError
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_products(self, name, page, per_page):
        return self.product_repository.get_products(name, page, per_page)

    def get_product_by_id(self, id):
        product = self.product_repository.get_product_by_id(id)

        if not product:
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        return product

    def product_exists_by_id(self, id):
        return self.product_repository.product_exists_by_id(id)

    def create_product(self, product):
        return self.product_repository.save_product(product)

    def update_product(self, id, product):
        if not self.product_exists_by_id(id):
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        product.id = id

        return self.product_repository.save_product(product)

    def delete_product_by_id(self, id):
        product = self.product_repository.get_product_by_id(id)

        if not product:
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        self.product_repository.delete_product_by_id(id)
