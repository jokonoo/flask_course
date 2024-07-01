import time

from flask import Flask
from flask_migrate import Migrate

from .api import blueprint as api_blueprint
from .api.movies.models import *


def create_app():
    app = Flask(__name__)
    migrate = Migrate(app, db)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@db/sw_db"

    app.register_blueprint(api_blueprint, url_prefix='/api')
    db.init_app(app)

    return app
