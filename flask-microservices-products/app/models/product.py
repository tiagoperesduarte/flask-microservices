import datetime

from app.config.database import db


class Product(db.Document):
    name = db.StringField()
    description = db.StringField()
    price = db.FloatField()
    created_on = db.DateTimeField(default=datetime.datetime.utcnow)

    @classmethod
    def from_dict(cls, data):
        return Product(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
