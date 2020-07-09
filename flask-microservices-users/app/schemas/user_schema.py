from marshmallow import Schema, fields


class UserQueryArgsSchema(Schema):
    name = fields.String()
    page = fields.Int()
    per_page = fields.Int()


class UserRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)


class UserResponseSchema(Schema):
    id = fields.String()
    name = fields.String()
    email = fields.String()
    created_on = fields.DateTime()
