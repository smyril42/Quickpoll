import os
from flask import Flask
from app.database import SQLiteHandler, db_init


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="jhvfawerklvbklgua",
        DATABASE=os.path.join(app.instance_path, "db.sqlite"),
        DATABASE_HANDLER=SQLiteHandler,
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db_init(app.config["DATABASE"], app.static_folder + "/schema.sql")

    # register blueprints
    from app.main import blueprint as blueprint_main
    from app.errorhandler import blueprint as blueprint_errorhandler

    app.register_blueprint(blueprint_main)
    app.register_blueprint(blueprint_errorhandler)

    return app
