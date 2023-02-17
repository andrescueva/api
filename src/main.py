from fastapi import FastAPI, Depends, Header
from starlette.exceptions import HTTPException
from src.api_keys import API_KEY
import jwt
from src.models import Message

app = FastAPI()


def validate_api_key(x_parse_rest_api_key: str = Header(...)):
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail=f"Invalid API KEY {API_KEY}")
    return x_parse_rest_api_key


@app.post("/DevOps/")
async def send_message(
    message: Message, x_parse_rest_api_key: str = Depends(validate_api_key)
):
    headers = {"x-parse-rest-api-key": x_parse_rest_api_key}
    message_dict = message.dict()
    to = message_dict["to"]
    return {"message": f"Hello {to} your message will be send", "headers": headers}


@app.get("/DevOps/")
async def send_message():
    raise HTTPException(status_code=405, detail="ERROR")


@app.delete("/DevOps/")
async def send_message():
    raise HTTPException(status_code=405, detail="ERROR")


@app.put("/DevOps/")
async def send_message():
    raise HTTPException(status_code=405, detail="ERROR")


@app.patch("/DevOps/")
async def send_message():
    raise HTTPException(status_code=405, detail="ERROR")


def create_jwt():
    payload = "ANY"
    jwt_token = jwt.encode(payload, "secret_key", algorithm="HS256")
    return jwt_token


async def get_token():
    token = create_jwt()

    return {"token": token}
