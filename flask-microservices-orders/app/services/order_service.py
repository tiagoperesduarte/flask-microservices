from app.errors.resource_not_found_error import ResourceNotFoundError
from app.repositories.order_repository import OrderRepository
from app.security.security_utils import SecurityUtils


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def get_orders(self, page, per_page):
        current_user = SecurityUtils.get_current_user()
        return self.order_repository.get_orders_by_user_id(current_user.id, page, per_page)

    def get_order_by_id(self, id):
        current_user = SecurityUtils.get_current_user()
        order = self.order_repository.get_order_by_id_and_user_id(id, current_user.id)

        if not order:
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        return order

    def create_order(self, order):
        current_user = SecurityUtils.get_current_user()

        order.id = None
        order.user_id = current_user.id

        return self.order_repository.save_order(order)

    def update_order(self, id, order):
        current_user = SecurityUtils.get_current_user()

        if not self.order_repository.order_exists_by_id_and_user_id(id, current_user.id):
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        order.id = id

        return self.order_repository.save_order(order)

    def delete_order_by_id(self, id):
        current_user = SecurityUtils.get_current_user()

        if not self.order_repository.order_exists_by_id_and_user_id(id, current_user.id):
            raise ResourceNotFoundError(f'Order not found with identifier {id}')

        self.order_repository.delete_order_by_id_and_user_id(id, current_user.id)
