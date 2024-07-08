from flask_restx import Resource

from .route import api
from .helpers import planet_page_data_parser


@api.route("/test")
class Test(Resource):
    def get(self):
        return {"test": "test"}


@api.route("/planet")
class PlanetView(Resource):
    def post(self):
        planet_page_data_parser(resource_type="planets")
