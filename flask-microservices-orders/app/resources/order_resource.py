from flask.views import MethodView
from flask_smorest import Blueprint

order_blp = Blueprint(
    'orders', 'orders', url_prefix='/api/orders'
)


@order_blp.route('')
class Orders(MethodView):
    ...


@order_blp.route('/<order_id>')
class OrdersById(MethodView):
    ...
