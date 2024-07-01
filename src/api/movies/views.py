from flask_restx import Namespace, Resource

from .helpers import data_request, planet_data_parser

api = Namespace('movies', description='Movies related operations')


@api.route("/test")
class Test(Resource):
    def get(self):
        return {"test": "test"}


@api.route("/planet")
class PlanetView(Resource):
    def post(self):
        data = data_request("planets")
        planet_data_parser(data)
