from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_user_signup():
    response = client.post(
        "/user/signup",
        json={
            "email": "test@a.com",
            "password": "sewsss",
            "user_name": "Drop the beat",
            "user_type": "email",
        },
    )

    assert response.status_code == 201
