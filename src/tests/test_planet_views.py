import os
from unittest import mock

import pytest


# class TestPlanetFetchView:
#     # @mock.patch()
#     def test_planet_fetching_post_view(self, client, add_planets):
#         pass
#         # with client as c:
#         #     response = c.post("/api/movies/planet/fetch")


class TestPlanetView:
    def test_planet_get_view(self, client, add_planets):
        with client as c:
            response = c.get("/api/movies/planet")
            assert response.status_code == 200
            assert len(response.json) == 10
