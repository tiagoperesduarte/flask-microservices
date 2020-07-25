from marshmallow import Schema, fields


class OrderItemRequestSchema(Schema):
    product_id = fields.String(required=True)
    quantity = fields.Int(required=True)


class OrderItemResponseSchema(Schema):
    product_id = fields.String()
    quantity = fields.Int()
