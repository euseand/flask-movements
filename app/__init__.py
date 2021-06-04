from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    with app.app_context():

        from app.common import api, db, migrate
        api.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)

        #from app.movements.model import db as movements_db
        #from app.movements.model import migrate as movements_migrate
        from app.movements.model import MoneyMovementModel
        from app.movements.controller import movement_blp, movements_blp

        #movements_migrate.init_app(app)
        api.register_blueprint(movement_blp)
        api.register_blueprint(movements_blp)


        #from app.users.model import db as users_db
        #from app.users.model import migrate as users_migrate
        from app.users.model import UserModel
        from app.users.controller import user_blp, users_blp

        #users_migrate.init_app(app)
        api.register_blueprint(user_blp)
        api.register_blueprint(users_blp)

    return app
