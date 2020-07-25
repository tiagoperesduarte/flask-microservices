from marshmallow import Schema, fields


class AuthRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class AuthResponseSchema(Schema):
    access_token = fields.String()
    refresh_token = fields.String()
