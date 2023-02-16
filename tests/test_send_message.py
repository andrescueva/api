from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_send_message_success():
    message =    {
        "message": "string",
        "to": "string",
        "from_": "string",
        "timeToLifeSec": 0
    }

    response = client.post("/DevOps", json = message)
    assert response.status_code == 200


