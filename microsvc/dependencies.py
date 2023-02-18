from fastapi import Header
from starlette.exceptions import HTTPException
import os
import jwt

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MIN = os.getenv("ACCESS_TOKEN_EXPIRE_MIN")


def validate_api_key(x_parse_rest_api_key: str = Header(...)):
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail=f"Invalid API KEY {API_KEY}")
    return x_parse_rest_api_key


def create_jwt():
    payload = {"key": "ANY"}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token
