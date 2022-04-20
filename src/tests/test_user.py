from pydantic import BaseModel
from typing import Optional
from starlette.testclient import TestClient

from src.main import app
from src.schemas.base_schemas import AllOptional

client = TestClient(app)

fake_db = {"email": "test@test.com", "password": "1q2w2e3r"}


class User(BaseModel):
    id: int
    email: str
    password: str
    user_name: Optional[str]
    user_type: str


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
    user_id = response.json()["id"]

    response_get = client.get(f"/users/{user_id}")
    assert response.json()["email"] == "test@a.com"
    assert response.json()["id"] == user_id
