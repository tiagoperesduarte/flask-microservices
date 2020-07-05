from flask_restful import Api


def configure_routes(app):
    from app.resources.product_resource import ProductResource
    from app.resources.product_resource import ProductListResource

    api = Api(app)
    api.add_resource(ProductResource, '/products/<string:id>')
    api.add_resource(ProductListResource, '/products')
