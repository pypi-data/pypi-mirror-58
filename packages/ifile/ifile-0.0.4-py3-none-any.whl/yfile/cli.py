import os
import sys
from shutil import copyfile
from functools import wraps

import click

from yfile import create_app, APP_HOME
from yfile.db.sqlalchemy.session import get_engine
from yfile.db.sqlalchemy.models import metadata


def with_app_context(func):
    @wraps(func)
    def inner(*args, **kwargs):
        app = create_app()
        app.app_context().push()

        return func(*args, **kwargs)
    return inner


@click.group()
def cli():
    """iFile command line tools"""


@click.group()
def db():
    """database manage tools"""


@cli.command()
def init():
    """init application."""
    app_home = APP_HOME
    if not os.path.exists(app_home):
        print(f"The directory '{app_home}' was created.")
        os.makedirs(app_home)

    config_file = os.path.join(app_home, 'ifile.ini')
    if not os.path.exists(config_file):
        default_config = os.path.join(
            os.path.dirname(__file__), 'default_config.ini')

        print(f"The config file '{config_file}' was created.")
        copyfile(default_config, config_file)

    print(f"Init completed! app_home is '{app_home}' .")


@cli.command()
@click.option("--debug/--no-debug", default=True, help="debug model.")
@click.option("--host", "-h", default='0.0.0.0', help="host address.")
@click.option("--port", "-p", default=5000, help="server port.")
def run(debug, host, port):
    """run server."""
    app = create_app()
    app.run(host=host, port=port, debug=debug)


@cli.command()
def details():
    """show application details."""
    print("\n      **APPLICATION DETAILS**      \n")

    print(" ========Configs========")
    from yfile import setting as config
    configs = [conf for conf in dir(config) if conf.isupper()]

    for conf in configs:
        value = getattr(config, conf)
        print(f" * {conf}: {value}")

    print(" =======================")


@db.command("init")
@with_app_context
def init_db():
    """init database, create tables."""
    engine = get_engine()
    metadata.create_all(engine)

    print("init database successful.")


cli.add_command(db)
