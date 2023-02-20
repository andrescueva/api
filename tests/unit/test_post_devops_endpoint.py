import os

def test_check_response_payload_from_send_message(message, client):
    """test success operation on post method to devops endpoint"""
    api_key = os.getenv("API_KEY")
    headers = {
        "x-parse-rest-api-key" : api_key,
        "Content-Type": "application/json",
        "accept": "application/json"
        }
    response = client.post("/DevOps/", json=message, headers=headers)
    expected_message = f"Hello {message['to']} your message will be send"
    assert response.json()["message"] == expected_message
    assert response.status_code == 200

