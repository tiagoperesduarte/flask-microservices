from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String()
    description = fields.String()
    price = fields.Float()
    created_on = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True
