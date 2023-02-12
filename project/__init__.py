import logging
import os
from logging.handlers import RotatingFileHandler

from click import echo
from flask import Flask

import project.db as db


# -------------
# Configuration
# -------------

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.


# ----------------------------
# Application Factory Function
# ----------------------------

def create_app(config_filename=None):
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    register_cli_commands(app)

    # # Check if the database needs to be initialized
    # engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    # inspector = sa.inspect(engine)
    # if not inspector.has_table("users"):
    #     with app.app_context():
    #         db.drop_all()
    #         db.create_all()
    #         app.logger.info('Initialized the database!')
    # else:
    #     app.logger.info('Database already contains the users table.')

    return app





def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo('Initialized the database!')
