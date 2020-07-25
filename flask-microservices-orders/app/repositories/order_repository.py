from flask_mongoengine import Pagination
from mongoengine import DoesNotExist, ValidationError

from app.models.order import Order


class OrderRepository:
    def get_orders(self, page, per_page):
        orders = Order.objects()
        return Pagination(orders, page, per_page).items

    def get_order_by_id(self, id):
        try:
            return Order.objects.get(id=id)
        except DoesNotExist:
            return None
        except ValidationError:
            return None

    def order_exists_by_id(self, id):
        order = self.get_order_by_id(id)

        if not order:
            return False

        return True

    def save_order(self, order):
        return order.save()

    def delete_order_by_id(self, id):
        Order.objects.get(id=id).delete()
