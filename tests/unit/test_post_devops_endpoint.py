

def test_send_message_status_code_200(message, client):
    response = client.post("/DevOps", json = message)
    assert response.status_code == 200


def test_check_response_payload_from_send_message(message, client):
    response = client.post("/DevOps", json=message)
    expected_message = f"Hello {message['to']} your message will be send"
    assert response.json()["message"] == expected_message


