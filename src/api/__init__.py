from flask import Blueprint
from flask_restx import Api

from .movies.movies import api as ns

blueprint = Blueprint('movies', __name__)


api = Api(blueprint, title="API", description="Main routes.")

api.add_namespace(ns)
