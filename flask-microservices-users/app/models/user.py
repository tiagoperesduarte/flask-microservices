import datetime

from app.configs.bcrypt_config import bcrypt
from app.configs.database_config import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField(unique=True)
    password = db.StringField()
    created_on = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_on = db.DateTimeField(default=datetime.datetime.utcnow)

    @classmethod
    def from_dict(cls, data):
        return User(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
