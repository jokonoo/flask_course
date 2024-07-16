import os
from unittest import mock

import pytest


class TestPlanetFetchView:
    @mock.patch("src.api.movies.views.request_page_data_parser")
    def test_planet_fetching_post_view(self, page_data_mock, client, add_planets, planets_dicts):
        with client as c:
            page_data_mock.return_value = planets_dicts
            response = c.post("/api/movies/planet/fetch")
            assert page_data_mock.called
            assert planets_dicts == response.json


class TestPlanetView:
    def test_planet_get_view(self, client, add_planets):
        with client as c:
            response = c.get("/api/movies/planet")
            assert response.status_code == 200
            assert len(response.json) == 10
