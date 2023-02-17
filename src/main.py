from fastapi import FastAPI, Depends, Header
from starlette.exceptions import HTTPException
import jwt
import os
from src.models import Message

API_KEY = os.getenv("API_KEY")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()


def validate_api_key(x_parse_rest_api_key: str = Header(...)):
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail=f"Invalid API KEY {API_KEY}")
    return x_parse_rest_api_key


@app.post("/DevOps/")
async def send_message(
    message: Message, x_parse_rest_api_key: str = Depends(validate_api_key)
):
    message_dict = message.dict()
    to = message_dict["to"]
    return {"message": f"Hello {to} your message will be send"}


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
    payload = {"key": "ANY"}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


@app.get("/jwt/")
async def get_token():
    token = create_jwt()
    return {"token": token}


@app.get("/health")
async def get_health_status():
    return {"status": "OK10"}
