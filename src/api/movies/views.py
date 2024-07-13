from flask_restx import abort, Resource

from database import db, get_or_create, get_first
from .models import CharacterModel, PlanetModel
from .route import api
from .helpers import request_page_data_parser
from .serializers import character_fetcher_serializer, character_serializer, planet_serializer, planet_fetcher_serializer


@api.route("/planet/fetch")
class PlanetFetchView(Resource):

    @api.marshal_with(planet_serializer)
    def post(self):
        request_page_data_parser(resource_type="planets")
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query


@api.route("/planet")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer, as_list=True)
    def get(self):
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query

    @api.expect(planet_fetcher_serializer, validate=True)
    @api.marshal_with(planet_serializer)
    def post(self):
        planet, created = get_or_create(PlanetModel, **api.payload)
        if created:
            return planet, 201
        else:
            abort(409, "Resource with that name already exist")


@api.route("/planet/<int:planet_id>")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def get(self, planet_id):
        planets_query = db.session.scalars(db.select(PlanetModel).filter_by(id=planet_id)).first()
        if not planets_query:
            pass
        return planets_query

    @api.expect()
    @api.marshal_with(planet_serializer)
    def put(self):
        pass


@api.route("/people/fetch")
class PeopleFetchView(Resource):

    @api.marshal_with(character_serializer, as_list=True)
    def post(self):
        request_page_data_parser(resource_type="people")
        people_query = db.session.scalars(db.select(CharacterModel)).all()
        return people_query


@api.route("/people")
class PeopleView(Resource):

    @api.marshal_with(character_serializer, as_list=True)
    def get(self):
        people_query = db.session.scalars(db.select(CharacterModel)).all()
        return people_query

    @api.expect(character_fetcher_serializer, validate=True)
    @api.marshal_with(character_serializer)
    def post(self):
        planet_object = get_first(PlanetModel, id=api.payload["planet_id"])
        if not planet_object:
            abort(404, "Planet object does not exist")
        people, created = get_or_create(CharacterModel, **api.payload)
        if created:
            return people, 201
        else:
            abort(409, "Resource with that name already exist")


@api.route("/people/<int:people_id>")
class PeopleView(Resource):

    @api.marshal_with(character_serializer, as_list=True)
    def get(self, people_id):
        people_query = db.session.scalars(db.select(CharacterModel).filter_by(id=people_id)).first()
        if not people_query:
            pass
        return people_query
