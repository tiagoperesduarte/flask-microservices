import datetime

from app.configs.database_config import db
from app.models.order_item import OrderItem


class Order(db.Document):
    user_id = db.StringField()
    items = db.ListField(db.EmbeddedDocumentField(OrderItem))
    comment = db.StringField()
    total = db.FloatField()
    created_on = db.DateTimeField(default=datetime.datetime.utcnow)

    @classmethod
    def from_dict(cls, data):
        items = [OrderItem.from_dict(data_item) for data_item in data['items']]

        return Order(
            items=items,
            comment=data.get('comment')
        )
