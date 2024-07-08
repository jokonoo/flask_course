from database import db


class PlanetModel(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    diameter = db.Column(db.BigInteger)
    population = db.Column(db.BigInteger)
    terrain = db.Column(db.String(200))
    residents = db.Relationship("CharacterModel", back_populates="planet")


class CharacterModel(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    planet = db.Relationship("PlanetModel", back_populates="residents")
