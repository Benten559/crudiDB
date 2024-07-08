from typing import Generator, Any
import pytest
from fastapi.testclient import TestClient
from server_app.main import app
from server_app.db.session import SessionLocal, Base, engine
from server_app.models.item import Item

client = TestClient(app)

# Create a test database session
def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() # type: ignore

app.dependency_overrides[override_get_db] = override_get_db

# Setup and teardown for tests
@pytest.fixture(scope="module")
def setup_database() -> Generator[None, Any, None]:
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_item(setup_database) -> None:
    response = client.post("/api/v1/items/", json={"name": "Test Item", "description": "A test item"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test item"
    assert "id" in data

def test_read_item(setup_database) -> None:
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test item"
    assert data["id"] == 1

def test_read_items(setup_database):
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Test Item"
    assert data[0]["description"] == "A test item"
    assert data[0]["id"] == 1
