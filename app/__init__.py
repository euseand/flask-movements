from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():

        from app.common import api, db, migrate, oauth
        api.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)
        oauth.init_app(app)
        oauth.register(
            name='google',
            server_metadata_url=app.config['GOOGLE_CONF_URL'],
            client_kwargs={
                'scope': 'openid email profile'
            }
        )

        from app.movements.models import MoneyMovementModel
        from app.movements.routes import movement_blp, movements_blp

        api.register_blueprint(movement_blp)
        api.register_blueprint(movements_blp)

        from app.users.models import UserModel
        from app.users.routes import auth_blp, google_blp

        api.register_blueprint(auth_blp)
        api.register_blueprint(google_blp)

    return app
