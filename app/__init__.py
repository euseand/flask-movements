from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_file_name):
    app = Flask(__name__)
    app.config.from_object(config_file_name)

    api = Api(app)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from app.views.movement import movement_blp, movements_blp
        api.register_blueprint(movement_blp)
        api.register_blueprint(movements_blp)

        return app
