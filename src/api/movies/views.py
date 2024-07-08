from flask_restx import Resource

from database import db
from .models import PlanetModel
from .route import api
from .helpers import planet_page_data_parser
from .serializers import planet_serializer


@api.route("/test")
class Test(Resource):
    def get(self):
        return {"test": "test"}


@api.route("/planet")
class PlanetView(Resource):
    @api.marshal_with(planet_serializer)
    def post(self):
        planet_page_data_parser(resource_type="planets")
        planets_query = db.session.scalars(db.select(PlanetModel)).all()
        return planets_query

