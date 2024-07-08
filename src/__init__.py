from flask import Flask
from flask_migrate import Migrate

from .api import blueprint as api_blueprint
from database import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@db/sw_db"

    app.register_blueprint(api_blueprint, url_prefix='/api')
    db.init_app(app)
    from .api.movies.models import PlanetModel, CharacterModel
    migrate = Migrate(app, db)

    return app
