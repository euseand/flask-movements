from flask import jsonify, url_for, session
from flask_smorest import abort, Blueprint

from app.users.schemas import UserSchema, UserInputSchema, UserSingleOutputSchema
from app.users.services import UserService
from app.users.exceptions import UserObjectNotFound
from app.common import oauth

auth_blp = Blueprint('auth', __name__, url_prefix='/auth',
                     description='Login/password authentication')
google_blp = Blueprint('auth/google', __name__, url_prefix='/auth/google',
                       description='Authentication via google')

user_dao = UserService()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

google = oauth.google


# Basic login/password auth
@auth_blp.route('/login', methods=['POST'])
@auth_blp.arguments(UserInputSchema)
@auth_blp.response(200)
def login(user_data):
    """Login via login/password

    Login with email/password.
    """
    try:
        user = user_dao.get_by_email(user_data.get('email'))
        if user and user.check_password(user_data.get('password')):
            session['user'] = user_schema.dump(user)
            print(session.get('user'))
            return {'message': 'Logged in successfully.'}, 200
        else:
            abort(401, message='Wrong password for this email.')
    except UserObjectNotFound:
        abort(404, message='User with this email does not exist.')


@auth_blp.arguments(UserSchema)
@auth_blp.response(201, UserSingleOutputSchema)
@auth_blp.route('/signup', methods=['POST'])
def signup(user_data):
    """Sign up as a new user

    Sign up with username, email and password
    """
    user = user_dao.get_by_username(user_data.get('username'))
    if user:
        abort(400, message='User with this username already exists.')

    user = user_dao.get_by_email(user_data.get('email'))
    if user:
        abort(400, message='User with this email address already exists.')

    user = user_dao.create(user_data)
    user_json = user_schema.dump(user)
    return jsonify({'user': user_json}), 201


@auth_blp.route('/logout', methods=['GET'])
def logout():
    """Logout

    Log out from session
    """
    session.pop('user', None)
    return {'message': 'Logged out successfully.'}, 200


# Google Login
@google_blp.route('/login', methods=['GET'])
def login():
    """Login via Google account

    Log in with Google credentials
    """
    redirect_uri = url_for('auth/google.callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@google_blp.route('/callback', methods=[])
def callback():
    """Function to claim user info from google oauth2

    Get user info from oauth2
    """
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    session['user'] = user
    return {'message': 'Logged in successfully.'}, 200
