import pytest
from starlette.testclient import TestClient

from app.core.config import create_engine, Session
from app.main import app


@pytest.fixture(scope="session")
def test_db_session():
    session = Session
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_app() -> TestClient:
    with TestClient(app=app()) as client:
        yield client
