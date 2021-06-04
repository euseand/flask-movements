from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():

        from app.common import api, db, migrate
        api.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)

        from app.movements.models import MoneyMovementModel
        from app.movements.routes import movement_blp, movements_blp

        api.register_blueprint(movement_blp)
        api.register_blueprint(movements_blp)

        from app.users.models import UserModel
        from app.users.routes import user_blp, users_blp
        
        api.register_blueprint(user_blp)
        api.register_blueprint(users_blp)

    return app
