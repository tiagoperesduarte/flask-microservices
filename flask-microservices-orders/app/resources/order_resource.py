from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from app.errors.resource_not_found_error import ResourceNotFoundError
from app.models.order import Order
from app.schemas.order_schema import OrderRequestSchema, OrderResponseSchema, OrderQueryArgsSchema
from app.services.order_service import OrderService

order_blp = Blueprint(
    'orders', 'orders', url_prefix='/api/orders'
)

order_service = OrderService()


@order_blp.route('', methods=['GET'])
@order_blp.arguments(OrderQueryArgsSchema, location='query')
@order_blp.response(OrderResponseSchema(many=True))
@jwt_required
def get_orders(args):
    page = args.get('page', 1)
    per_page = args.get('per_page', 10)

    return order_service.get_orders(page, per_page)


@order_blp.route('/<order_id>', methods=['GET'])
@order_blp.response(OrderResponseSchema)
@jwt_required
def get_order_by_id(order_id):
    try:
        return order_service.get_order_by_id(order_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@order_blp.route('', methods=['POST'])
@order_blp.arguments(OrderRequestSchema)
@order_blp.response(OrderResponseSchema, code=201)
@jwt_required
def create_order(data):
    order = Order.from_dict(data)
    return order_service.create_order(order)


@order_blp.route('/<order_id>', methods=['PUT'])
@order_blp.arguments(OrderRequestSchema)
@order_blp.response(OrderResponseSchema)
@jwt_required
def update_order(data, order_id):
    try:
        order = Order.from_dict(data)
        return order_service.update_order(order_id, order)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))


@order_blp.route('/<order_id>', methods=['DELETE'])
@order_blp.response(code=204)
@jwt_required
def delete_order_by_id(order_id):
    try:
        order_service.delete_order_by_id(order_id)
    except ResourceNotFoundError as e:
        abort(404, message=str(e))
