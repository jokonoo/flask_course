from flask_restx import fields

from .route import api

character_serializer = api.model("Character", {
    "id": fields.Integer(),
    "name": fields.String(),
    "planet_id": fields.Integer(),
})

character_fetcher_serializer = api.model("CharacterInput", {
    "name": fields.String(required=True),
    "planet_id": fields.Integer(required=True, min=1),
}, strict=True)

character_put_serializer = api.model("CharacterInput", {
    "name": fields.String(),
    "planet_id": fields.Integer(min=1),
}, strict=True)

planet_serializer = api.model("Planet", {
    "id": fields.Integer(),
    "name": fields.String(),
    "diameter": fields.Integer(min=0),
    "population": fields.Integer(min=0),
    "terrain": fields.String(),
    "residents": fields.Nested(character_serializer, as_list=True)
})

planet_fetcher_serializer = api.model("PlanetInput", {
    "name": fields.String(required=True),
    "diameter": fields.Integer(min=0),
    "population": fields.Integer(min=0),
    "terrain": fields.String(),
}, strict=True)

planet_put_serializer = api.model("PlanetPut", {
    "name": fields.String(),
    "diameter": fields.Integer(min=0),
    "population": fields.Integer(min=0),
    "terrain": fields.String(),
}, strict=True)
