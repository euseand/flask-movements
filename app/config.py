from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))


class Config:
    # base config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    CSRF_ENABLED = True

    # DB config
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API config
    API_TITLE = environ.get('API_TITLE')
    API_VERSION = environ.get('API_VERSION')
    OPENAPI_VERSION = environ.get('OPENAPI_VERSION')
    OPENAPI_URL_PREFIX = environ.get('OPENAPI_URL_PREFIX')
    OPENAPI_SWAGGER_UI_PATH = environ.get('OPENAPI_SWAGGER_UI_PATH')
    OPENAPI_SWAGGER_UI_URL = environ.get('OPENAPI_SWAGGER_UI_URL')
    OPENAPI_REDOC_PATH = environ.get('OPENAPI_REDOC_PATH')
    OPENAPI_REDOC_URL = environ.get('OPENAPI_REDOC_URL')
    OPENAPI_RAPIDOC_PATH = environ.get('OPENAPI_RAPIDOC_PATH')
    OPENAPI_RAPIDOC_URL = environ.get('OPENAPI_RAPIDOC_URL')

