from app.users.model import db, UserModel
from app.users.exceptions import UserObjectNotFound


class UserService:
    """Manager class for User objects"""

    @staticmethod
    def get_all():
        """Read all User objects from database"""
        users_list = UserModel.query.all()
        return users_list

    @staticmethod
    def get_by_id(user_id):
        """Read a single User object from database by id"""
        user = UserModel.query.filter_by(user_id=user_id).first()
        if user:
            return user
        else:
            raise UserObjectNotFound

    @staticmethod
    def get_by_username(username):
        """Read a single User object from database by username"""
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return user
        else:
            raise UserObjectNotFound

    @staticmethod
    def get_by_email(email):
        """Read a single User object from database by email"""
        user = UserModel.query.filter_by(email=email).first()
        if user:
            return user
        else:
            raise UserObjectNotFound

    @staticmethod
    def create(data):
        """Create a new object and save to database"""
        user = UserModel(username=data.get('username'), email=data.get('email'))
        user.set_password(data.get('password'))
        db.session.add(user)
        db.session.commit()
        return user
