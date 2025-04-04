import pytest

from flask.testing import FlaskClient
from api.run import app
from postgresql_db.database import Base, engine
from werkzeug.test import TestResponse


@pytest.fixture
def client():
    app.config["TESTING"] = True

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with app.test_client() as client:
        yield client


def test_signup_and_login(client: FlaskClient) -> None:
    response: TestResponse = client.post(
        "/auth/signup",
        json={
            "username": "testuser",
            "password": "testpass",
        },
    )
    assert response.status_code == 201

    response: TestResponse = client.post(
        "/auth/login",
        json={
            "username": "testuser",
            "password": "testpass",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.get_json()
