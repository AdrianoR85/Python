from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import click
import os

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

@click.command('init-db')
def init_db_command():
    global db
    click.echo('Initialized the database.')
    with current_app.app_context():
        db.create_all()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= 'data/diobank.sqlite',

    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs('data')
    except OSError:
        pass
    
    # register the database commands
    app.cli.add_command(init_db_command)

    # initialize Extensions
    db.init_app(app)
    
    return app

