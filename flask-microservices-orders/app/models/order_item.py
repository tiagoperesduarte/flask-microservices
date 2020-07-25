from app.config.database import db


class OrderItem(db.EmbeddedDocument):
    product_id = db.StringField()
    quantity = db.IntField()

    @classmethod
    def from_dict(cls, data):
        return OrderItem(
            product_id=data['product_id'],
            quantity=data['quantity']
        )
