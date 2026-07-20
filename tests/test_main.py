import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"DevSecOps Platform" in rv.data

def test_health(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.json == {"status": "healthy"}

def test_status(client):
    rv = client.get("/api/v1/status")
    assert rv.status_code == 200
    assert "service" in rv.json
    assert "version" in rv.json
    assert "environment" in rv.json
