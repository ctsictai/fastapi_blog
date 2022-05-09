from pydantic import BaseModel
from typing import Optional
from starlette.testclient import TestClient

from src.main import app
from jose import JWTError, jwt
from passlib.context import CryptContext

client = TestClient(app)

fake_db = {
    "email": "test@test.com", 
    "password": "1q2w2e3r", 
    "user_type" : "email",
    "user_name" : "test_user",
}


class User(BaseModel):
    id: int
    email: str
    password: str
    user_name: Optional[str]
    user_type: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_name: str | None = None
    user_type: str | None = None

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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, email:str):
    if email in db:
        user_dict = db[email]
        return db

def authenticate_user(fake_db, email: str, password: str):
    user = get_user(fake_db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
