from flask import session
from flask_smorest import abort


def auth_required(func):
    def wrapper(*args, **kwargs):
        if session.get('user'):
            return func(*args, **kwargs)
        else:
            abort(401, message='You have to be authorized to do this')
    return wrapper
