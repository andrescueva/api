import pytest
from fastapi.testclient import TestClient
from src.main import app



@pytest.fixture
def message():
    message =    {
        "message": "Any Message",
        "to": "Any Name",
        "from_": "Any Source",
        "timeToLifeSec": 1
    }
    return message


@pytest.fixture
def client():
    client = TestClient(app)
    return client
