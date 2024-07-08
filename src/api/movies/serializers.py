from flask_restx import fields

from .route import api

character_serializer = api.model("Character", {
    "id": fields.Integer(readonly=True),
    "name": fields.String(required=True),
    "planet_id": fields.Integer(required=True),
})

character_fetcher_serializer = api.model("Character", {
    "name": fields.String(required=True),
    "planet_id": fields.Integer(required=True),
})

planet_serializer = api.model("Planet", {
    "id": fields.Integer(readonly=True),
    "name": fields.String(),
    "diameter": fields.Integer(),
    "population": fields.Integer(min=0),
    "terrain": fields.String(),
    "residents": fields.Nested(character_serializer, as_list=True, readonly=True)
})

planet_fetcher_serializer = api.model("Planet", {
    "name": fields.String(),
    "diameter": fields.Integer(),
    "population": fields.Integer(min=0),
    "terrain": fields.String(),
})



