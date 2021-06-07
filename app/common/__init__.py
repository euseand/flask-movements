from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth

api = Api()
db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()


