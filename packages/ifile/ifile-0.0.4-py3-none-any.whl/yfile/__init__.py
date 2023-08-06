import os

from flask import Flask

from yfile.db.base import DataBase

database = DataBase()


def create_app():
    app = Flask(__name__)

    from yfile import setting as config
    app.config.from_object(config)

    database.init_app(app)

    from yfile.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


def get_app_home():
    """get application home path"""
    app_home = os.path.expanduser(
        os.path.expandvars(os.environ.get('IFILE_HOME', '~/ifile')))
    return app_home

APP_HOME = get_app_home()
