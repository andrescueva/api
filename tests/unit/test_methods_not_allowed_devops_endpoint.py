def test_get_error_messages_to_get_method(client):
    reponse = client.get("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"


def test_get_error_messages_to_put_method(client):
    reponse = client.put("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"



def test_get_error_messages_to_delete_method(client):
    reponse = client.delete("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"
