from extensions import db


class PlanetModel(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(200))
    residents = db.Relationship("CharacterModel", back_populates="planet", lazy="dynamic")


class CharacterModel(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    planet = db.Relationship("PlanetModel", back_populates="characters")
