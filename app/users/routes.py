from flask import jsonify
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from app.users.schemas import UserSchema, UserSingleOutputSchema, UserListOutputSchema
from app.users.services import UserService
from app.users.exceptions import UserObjectNotFound, UserObjectAlreadyExists


user_blp = Blueprint('user', __name__, url_prefix='/users',
                     description='All operations for a single user object')
users_blp = Blueprint('users', __name__, url_prefix='/users',
                      description='All operations for a list of user objects')

user_dao = UserService()

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_blp.route('/<user_id>')
class Movement(MethodView):
    """Api view class for single User object operations"""

    @staticmethod
    @user_blp.response(200, UserSingleOutputSchema)
    def get(user_id):
        """Read a single user

        Return single user object.
        """
        try:
            user = user_dao.get_by_id(user_id)
            user_json = user_schema.dump(user)
            return jsonify({'user': user_json}), 200
        except UserObjectNotFound:
            abort(404, message='User not found.')


@users_blp.route('/')
class UsersList(MethodView):
    """Api view class for a list of User objects operations"""

    @staticmethod
    @users_blp.response(200, UserListOutputSchema)
    def get():
        """Read all users

        Return all user objects.
        """
        users = user_dao.get_all()
        users_json = users_schema.dump(users)
        return jsonify({'users': users_json}), 200

    @staticmethod
    @users_blp.arguments(UserSchema)
    @users_blp.response(201, UserSingleOutputSchema)
    def post(user_data):
        """Create a new user

        Add a new user object.
        """
        try:
            user_dao.get_by_email(user_data.get('email'))
        except UserObjectAlreadyExists:
            abort(400, message='User with this email address already exists.')
        except UserObjectNotFound:
            pass
        try:
            user_dao.get_by_username(user_data.get('username'))
        except UserObjectAlreadyExists:
            abort(400, message='User with this username already exists.')
        except UserObjectNotFound:
            pass
        user = user_dao.create(user_data)
        user_json = user_schema.dump(user)
        return jsonify({'user': user_json}), 201
