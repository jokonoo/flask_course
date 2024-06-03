from flask import Flask
from .api import blueprint as api_blueprint
from .extensions import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@db:5432/movie_db"

    app.register_blueprint(api_blueprint, url_prefix='/api')
    db.init_app(app)

    return app
