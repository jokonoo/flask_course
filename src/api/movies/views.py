from flask_restx import Resource

from database import db
from .models import CharacterModel, PlanetModel
from .route import api
from .helpers import request_page_data_parser
from .serializers import character_serializer, planet_serializer


@api.route("/planet/fetch")
class PlanetFetchView(Resource):

    @api.marshal_with(planet_serializer)
    def post(self):
        request_page_data_parser(resource_type="planets")
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query


@api.route("/planet")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def get(self):
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query

    @api.marshal_with(planet_serializer)
    def post(self):
        pass


@api.route("/planet/<int:planet_id>")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def get(self, planet_id):
        planets_query = db.session.scalars(db.select(PlanetModel).filter_by(id=planet_id)).first()
        if not planets_query:
            pass
        return planets_query


@api.route("/people/fetch")
class PeopleFetchView(Resource):

    @api.marshal_with(character_serializer)
    def post(self):
        request_page_data_parser(resource_type="people")
        people_query = db.session.scalars(db.select(CharacterModel)).all()
        return people_query


@api.route("/people")
class PeopleView(Resource):

    @api.marshal_with(character_serializer)
    def get(self):
        people_query = db.session.scalars(db.select(CharacterModel)).all()
        return people_query

    @api.marshal_with(character_serializer)
    def post(self):
        pass


@api.route("/people/<int:people_id>")
class PeopleView(Resource):

    @api.marshal_with(character_serializer)
    def get(self, people_id):
        people_query = db.session.scalars(db.select(CharacterModel).filter_by(id=people_id)).first()
        if not people_query:
            pass
        return people_query

