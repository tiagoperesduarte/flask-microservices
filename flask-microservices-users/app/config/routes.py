from flask_smorest import Api


def configure_routes(app):
    app.config['API_TITLE'] = 'API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'

    from app.resources.user_resource import user_blp

    api = Api(app)
    api.register_blueprint(user_blp)
