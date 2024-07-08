from flask_restx import Resource

from database import db
from .models import CharacterModel, PlanetModel
from .route import api
from .helpers import request_page_data_parser
from .serializers import character_serializer, planet_serializer


@api.route("/planet")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def post(self):
        request_page_data_parser(resource_type="planets")
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query


@api.route("/people")
class PeopleView(Resource):
    @api.marshal_with(character_serializer)
    def post(self):
        request_page_data_parser(resource_type="people")
        people_query = db.session.scalars(db.select(CharacterModel)).all()
        return people_query

