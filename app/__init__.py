from secrets import token_urlsafe
from os.path import join as join_path
from pathlib import Path
from flask import Flask
from flask_login import LoginManager

from .database import db, User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # create instance directory if not exists
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    # get secret, generate if not exists
    secret_path = join_path(app.instance_path, 'SECRET')
    try:
        with app.open_instance_resource("SECRET", "rb") as f:
            secret_key = f.read().decode('utf-8')
    except FileNotFoundError:
        with app.open_instance_resource(secret_path, 'xb') as f:
            secret_key = token_urlsafe()
            f.write(secret_key.encode('utf-8'))
            print(f"Created secret key at {secret_path}")

    app.config.from_mapping(
        SECRET_KEY=secret_key,
        DATABASE=join_path(app.instance_path, "main.db"),
        SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
    )

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.init_app(app)
        db.create_all()

    # register blueprints
    from .main import bp as bp_main
    from .errorhandler import bp as bp_errorhandler
    from .auth import bp as bp_auth
    from .admin import bp as bp_admin

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_errorhandler)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_admin)

    return app
