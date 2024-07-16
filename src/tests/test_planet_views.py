import pytest


class TestPlanetView:
    def test_planet_fetching_get_view(self, client, planets):
        with client as c:
            response = c.get("/api/movies/planet")
            assert response.status_code == 200
            assert len(response.json) == 10
