import requests

BASE_URL = "https://swapi.dev/api/"


def data_request(resource):
    url = f"{BASE_URL}{resource}/"
    return requests.get(url).json()


def planet_data_parser(data):
    print(data)
    print(data["count"])
