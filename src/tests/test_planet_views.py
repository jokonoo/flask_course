def test_home(client):
    with client as c:
        response = c.get("/api/movies/planet")
        assert response.status_code == 200
