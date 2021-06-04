from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    date_joined = db.Column(db.Date, unique=False, nullable=False, default=datetime.datetime.today)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User : {self.email} : {self.username}'
