from app.errors.resource_not_found_error import ResourceNotFoundError
from app.repositories.product_repository import ProductRepository
from app.security.security_utils import SecurityUtils


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_products(self, name, page, per_page):
        current_user = SecurityUtils.get_current_user()
        return self.product_repository.get_products_by_user_id(current_user.id, name, page, per_page)

    def get_product_by_id(self, id):
        current_user = SecurityUtils.get_current_user()
        product = self.product_repository.get_product_by_id_and_user_id(id, current_user.id)

        if not product:
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        return product

    def create_product(self, product):
        current_user = SecurityUtils.get_current_user()

        product.id = None
        product.user_id = current_user.id

        return self.product_repository.save_product(product)

    def update_product(self, id, product):
        current_user = SecurityUtils.get_current_user()

        if not self.product_repository.product_exists_by_id_and_user_id(id, current_user.id):
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        product.id = id

        return self.product_repository.save_product(product)

    def delete_product_by_id(self, id):
        current_user = SecurityUtils.get_current_user()

        if not self.product_repository.product_exists_by_id_and_user_id(id, current_user.id):
            raise ResourceNotFoundError(f'Product not found with identifier {id}')

        self.product_repository.delete_product_by_id_and_user_id(id, current_user.id)
