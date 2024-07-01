from flask import Blueprint
from flask_restx import Api

from .movies.views import api as ns

blueprint = Blueprint('api', __name__)


api = Api(blueprint, title="API", description="Main routes.")

api.add_namespace(ns)
