from app.errors.resource_not_found_error import ResourceNotFoundError
from app.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def get_orders(self, page, per_page):
        return self.order_repository.get_orders(page, per_page)

    def get_order_by_id(self, id):
        order = self.order_repository.get_order_by_id(id)

        if not order:
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        return order

    def order_exists_by_id(self, id):
        return self.order_repository.order_exists_by_id(id)

    def create_order(self, order):
        return self.order_repository.save_order(order)

    def update_order(self, id, order):
        if not self.order_exists_by_id(id):
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        order.id = id

        return self.order_repository.save_order(order)

    def delete_order_by_id(self, id):
        order = self.order_repository.get_order_by_id(id)

        if not order:
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        self.order_repository.delete_order_by_id(id)
