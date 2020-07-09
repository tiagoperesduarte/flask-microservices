import datetime

from app.config.database import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    created_on = db.DateTimeField(default=datetime.datetime.utcnow)

    @classmethod
    def from_dict(cls, data):
        return User(
            name=data['name'],
            email=data['email']
        )
