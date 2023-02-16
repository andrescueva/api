
from fastapi import (
    FastAPI,
    Depends,
    Header
    )

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
import os
import jwt
from src.models import Message

app = FastAPI()

API_KEY_ENPOINT = os.getenv("API_KEY_ENDPOINT")



def validate_api_key(api_key: str = Header(...)):
    if api_key != API_KEY_ENPOINT:
        raise HTTPException(status_code=401, detail="Invalida API KEY")
    return api_key


@app.post("/DevOps/")
async def send_message(message: Message):
    message_dict = message.dict()
    to = message_dict['to']
    return {"message": f"Hello {to} your message will be send"}


@app.exception_handler(HTTPException)
async def raise_not_allowed_methods(request, exc):
    return JSONResponse(
        status_code=405,
        content={"detail": "ERROR"}
    )


def create_jwt():
    payload = "ANY"
    jwt_token = jwt.encode(payload, "secret_key", algorithm = "HS256")
    return jwt_token

async def get_token():
    token = create_jwt()

    return {"token": token}
