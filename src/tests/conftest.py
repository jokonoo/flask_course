import pytest
from flask_migrate import upgrade
from sqlalchemy import delete, text

from database import db
from src import create_app
from src.api.movies.models import CharacterModel, PlanetModel


@pytest.fixture(autouse=True, scope="session")
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
def planets():
    planet_models = [
        PlanetModel(name=f"test_planet_{object_number}",
                    diameter=object_number * 1000,
                    population=object_number * 1000,
                    terrain="test_value") for object_number in range(10)]
    return planet_models


@pytest.fixture()
def add_planets(app, planets):
    with app.app_context():
        db.session.add_all(planets)
        db.session.commit()
        yield db.session.scalars(db.select(PlanetModel)).all()
        db.session.execute(delete(PlanetModel))
        db.session.commit()

