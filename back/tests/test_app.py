import pytest
from app import app
from flask.testing import FlaskClient


@pytest.fixture
def client():
    """Create a Flask client test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_visualize_official_success(client: FlaskClient):
    """Test if the route return a correct JSON."""
    response = client.post("/visualize-official", json={"set_name": "mrd"})
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert "rarity_cardinal" in data
