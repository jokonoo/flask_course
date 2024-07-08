import requests
from requests.exceptions import JSONDecodeError

from flask_restx.fields import MarshallingError
from .models import PlanetModel
from .exceptions import NoResourceValue, WrongUrlResourceNotFound
from .serializers import planet_fetcher_serializer
from .route import api

from database import get_or_create

BASE_URL = "https://swapi.dev/api/"


def data_request(resource=None, url=None):
    if not url:
        if not resource:
            raise NoResourceValue("If not url provided, then resource parameter must be defined")
        url = f"{BASE_URL}{resource}/"
    try:
        return requests.get(url).json()
    except JSONDecodeError:
        raise WrongUrlResourceNotFound


def planet_data_parser(data):
    for planet_object in data:
        planet_object_dict = {
            "name": planet_object.get("name"),
            "diameter": planet_object.get("diameter") if planet_object.get("diameter") != "unknown" else None,
            "population": planet_object.get("population") if planet_object.get("population") != "unknown" else None,
            "terrain": planet_object.get("terrain") if planet_object.get("terrain") != "unknown" else None
        }
        try:
            validated_data = api.marshal(planet_object_dict, planet_fetcher_serializer, skip_none=True)
            get_or_create(PlanetModel, **validated_data)
        except MarshallingError:
            pass


def planet_page_data_parser(resource_type: str) -> None:
    data = data_request(resource=resource_type)
    next_page = data.get("next")
    planet_data_parser(data["results"])
    while next_page:
        data = data_request(url=next_page)
        planet_data_parser(data["results"])
        next_page = data.get("next")
