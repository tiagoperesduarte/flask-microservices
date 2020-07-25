from marshmallow import Schema, fields

from app.schemas.order_item_schema import OrderItemRequestSchema, OrderItemResponseSchema


class OrderQueryArgsSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()


class OrderRequestSchema(Schema):
    items = fields.List(
        fields.Nested(OrderItemRequestSchema()),
        required=True
    )


class OrderResponseSchema(Schema):
    id = fields.String()
    user_id = fields.String()
    items = fields.List(fields.Nested(OrderItemResponseSchema()))
    created_on = fields.DateTime()
