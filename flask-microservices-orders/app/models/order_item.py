from app.config.database_config import db


class OrderItem(db.EmbeddedDocument):
    product_id = db.StringField()
    quantity = db.IntField()
    price = db.FloatField()
    total = db.FloatField()

    @classmethod
    def from_dict(cls, data):
        return OrderItem(
            product_id=data['product_id'],
            quantity=data['quantity']
        )
