import pytest

from flask.testing import FlaskClient
from api.run import app
from database.connection import Base, engine
from werkzeug.test import TestResponse


@pytest.fixture
def client():
    app.config["TESTING"] = True

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with app.test_client() as client:
        yield client


def test_signup_and_login(client: FlaskClient) -> None:
    response_signup: TestResponse = client.post(
        "/auth/signup",
        json={
            "username": "testuser",
            "password": "testpass",
        },
    )
    assert response_signup.status_code == 201

    response_login: TestResponse = client.post(
        "/auth/login",
        json={
            "username": "testuser",
            "password": "testpass",
        },
    )
    assert response_login.status_code == 200
    assert "access_token" in response_login.get_json()
