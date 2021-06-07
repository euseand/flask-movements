from flask import jsonify, url_for, session, redirect, flash
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from app.users.schemas import UserSchema, UserSingleOutputSchema, UserListOutputSchema
from app.users.services import UserService
from app.users.exceptions import UserObjectNotFound, UserObjectAlreadyExists
from app.common import oauth

user_blp = Blueprint('user', __name__, url_prefix='/users',
                     description='All operations for a single user object')
users_blp = Blueprint('users', __name__, url_prefix='/users',
                      description='All operations for a list of user objects')
auth_blp = Blueprint('auth', __name__, url_prefix='/auth',
                     description='All authentication operations')

user_dao = UserService()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

google = oauth.google


@users_blp.route('/')
class UsersList(MethodView):
    """Api view class for a list of User objects operations"""

    @staticmethod
    @users_blp.response(200, UserListOutputSchema)
    def get():
        """Read all users

        Return all user objects.
        """
        user = session.get('user')
        if user:
            users = user_dao.get_all()
            users_json = users_schema.dump(users)
            return jsonify({'users': users_json}), 200
        else:
            abort(401, message='You have to be authorized to do this.')


@auth_blp.route('/login')
def login():
    """Login user

    Log in to a session
    """
    redirect_uri = url_for('auth.callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_blp.route('/callback')
def callback():
    """Function to claim user info from google oauth2

    Get user info from oauth2
    """
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    session['user'] = user
    return redirect(url_for('users.UsersList'))


@auth_blp.route('/logout')
def logout():
    """Logout user

    Log out from session
    """
    session.pop('user', None)
    return {'message': 'Logged out successfully'}, 200


@auth_blp.arguments(UserSchema)
@auth_blp.response(201, UserSingleOutputSchema)
@auth_blp.route('/signup', methods=['POST'])
def signup(user_data):
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
