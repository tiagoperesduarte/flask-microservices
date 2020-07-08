from flask_smorest import Api


def configure_routes(app):
    app.config['OPENAPI_VERSION'] = '3.0.2'

    from app.resources.product_resource import product_blp

    api = Api(app)
    api.register_blueprint(product_blp)
