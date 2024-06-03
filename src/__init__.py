from flask import Flask
from .api import blueprint as api_blueprint
from .extensions import db
import time


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@db/sw_db"

    app.register_blueprint(api_blueprint, url_prefix='/api')
    db.init_app(app)
    time.sleep(10)  # TODO add entrypoint script to wait for database

    with app.app_context():
        db.create_all()

    return app
