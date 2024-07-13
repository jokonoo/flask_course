import os

from flask import Flask
from flask_migrate import Migrate

from .api import blueprint as api_blueprint
from database import db


# DATABASE ENVIRONMENTAL VARIABLES

DB_HOST = os.getenv("POSTGRES_HOST")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_DATABASE = os.getenv("POSTGRES_DB")


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
    app.config["RESTX_ERROR_404_HELP"] = False

    app.register_blueprint(api_blueprint, url_prefix='/api')
    db.init_app(app)
    from .api.movies.models import PlanetModel, CharacterModel
    migrate = Migrate(app, db)

    return app
