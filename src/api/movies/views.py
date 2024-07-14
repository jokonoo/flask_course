from flask_restx import abort, Resource

from database import db, get_or_create, get_first
from .exceptions import RESOURCE_DOES_NOT_EXIST_MESSAGE, RESOURCE_ALREADY_EXIST
from .models import CharacterModel, PlanetModel
from .route import api
from .helpers import check_name_unique, request_page_data_parser
from .serializers import (character_fetcher_serializer,
                          character_put_serializer,
                          character_serializer,
                          planet_serializer,
                          planet_fetcher_serializer,
                          planet_put_serializer)


@api.route("/planet/fetch")
class PlanetFetchView(Resource):

    @api.marshal_with(planet_serializer)
    def post(self):
        request_page_data_parser(resource_type="planets")
        planets_query = db.session.scalars(db.select(PlanetModel).order_by(PlanetModel.id)).all()
        return planets_query


@api.route("/planet")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer, as_list=True)
    def get(self):
        planets_query = db.session.scalars(db.select(PlanetModel).order_by(PlanetModel.id)).all()
        return planets_query

    @api.expect(planet_fetcher_serializer, validate=True)
    @api.marshal_with(planet_serializer)
    def post(self):
        planet, created = get_or_create(PlanetModel, **api.payload)
        if created:
            return planet, 201
        else:
            abort(409, RESOURCE_ALREADY_EXIST)


@api.route("/planet/<int:planet_id>")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def get(self, planet_id):
        planet_object = get_first(PlanetModel, id=planet_id)
        if not planet_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        return planet_object

    @api.expect(planet_put_serializer, validate=True)
    @api.marshal_with(planet_serializer)
    def patch(self, planet_id):
        planet_object = get_first(PlanetModel, id=planet_id)
        if not planet_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        for attr_key, attr_value in api.payload.items():
            planet_name_exist = check_name_unique(PlanetModel, attr_key, attr_value)
            if planet_name_exist:
                abort(409, RESOURCE_ALREADY_EXIST)
            setattr(planet_object, attr_key, attr_value)
        db.session.commit()
        return planet_object

    def delete(self, planet_id):
        planet_object = get_first(PlanetModel, id=planet_id)
        if not planet_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        db.session.delete(planet_object)
        db.session.commit()
        return {}, 204


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
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        people, created = get_or_create(CharacterModel, **api.payload)
        if created:
            return people, 201
        else:
            abort(409, RESOURCE_ALREADY_EXIST)


@api.route("/people/<int:people_id>")
class PeopleView(Resource):

    @api.marshal_with(character_serializer, as_list=True)
    def get(self, people_id):
        people_object = get_first(CharacterModel, id=people_id)
        if not people_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        return people_object

    @api.expect(character_put_serializer, validate=True)
    @api.marshal_with(character_serializer)
    def patch(self, people_id):
        people_object = get_first(CharacterModel, id=people_id)
        if not people_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        for attr_key, attr_value in api.payload.items():
            people_name_exist = check_name_unique(CharacterModel, attr_key, attr_value)
            if people_name_exist:
                abort(409, RESOURCE_ALREADY_EXIST)
            setattr(people_object, attr_key, attr_value)
        db.session.commit()
        return people_object

    def delete(self, people_id):
        people_object = get_first(CharacterModel, id=people_id)
        if not people_object:
            abort(404, RESOURCE_DOES_NOT_EXIST_MESSAGE)
        db.session.delete(people_object)
        db.session.commit()
        return {}, 204
