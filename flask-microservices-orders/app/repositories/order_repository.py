from flask_mongoengine import Pagination
from mongoengine import DoesNotExist, ValidationError

from app.models.order import Order


class OrderRepository:
    def get_orders_by_user_id(self, user_id, page, per_page):
        orders = Order.objects(user_id=user_id)
        return Pagination(orders, page, per_page).items

    def get_order_by_id_and_user_id(self, id, user_id):
        try:
            return Order.objects.get(id=id, user_id=user_id)
        except DoesNotExist:
            return None
        except ValidationError:
            return None

    def order_exists_by_id_and_user_id(self, id, user_id):
        order = self.get_order_by_id_and_user_id(id, user_id)

        if not order:
            return False

        return True

    def save_order(self, order):
        return order.save()

    def delete_order_by_id_and_user_id(self, id, user_id):
        Order.objects.get(id=id, user_id=user_id).delete()
