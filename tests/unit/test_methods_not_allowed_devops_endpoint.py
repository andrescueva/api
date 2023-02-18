def test_error_message_from_get_method(client):
    reponse = client.get("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"


def test_error_messages_from_put_method(client):
    reponse = client.put("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"


def test_error_message_from_delete_method(client):
    reponse = client.delete("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"

def test_error_message_from_patch_method(client):
    reponse = client.patch("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"
