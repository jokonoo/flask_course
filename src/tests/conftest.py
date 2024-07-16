import time

import pytest
from flask_migrate import upgrade
from sqlalchemy import text

from database import db
from src import create_app
from src.api.movies.models import CharacterModel, PlanetModel

planet_objects = [
    PlanetModel(name=f"test_planet_{object_number}",
                diameter=object_number*1000,
                population=object_number*1000,
                terrain="test_value") for object_number in range(10)]


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    with app.app_context():
        upgrade(directory="migrations")
    yield app
    with app.app_context():
        db.drop_all()
        with db.engine.begin() as conn:
            conn.execute(text("DROP TABLE alembic_version"))


@pytest.fixture()
def client(app):
    yield app.test_client()


@pytest.fixture()
def add_planets(app):
    with app.app_context():
        db.session.add_all(planet_objects)
        db.session.commit()
        return app


@pytest.fixture()
def planets(add_planets):
    app_instance = add_planets
    with app_instance.app_context():
        return db.session.scalars(db.select(PlanetModel)).all()
