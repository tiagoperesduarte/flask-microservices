from marshmallow import Schema, fields


class ProductQueryArgsSchema(Schema):
    name = fields.String()
    page = fields.Int()
    per_page = fields.Int()


class ProductRequestSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)


class ProductResponseSchema(Schema):
    id = fields.String()
    name = fields.String()
    description = fields.String()
    price = fields.Float()
    created_on = fields.DateTime()
