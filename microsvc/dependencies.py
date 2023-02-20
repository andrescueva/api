"""dependencies module
"""
import os
import jwt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MIN = os.getenv("ACCESS_TOKEN_EXPIRE_MIN")


def validate_api_key(x_parse_rest_api_key: str):
    """Validate api key """
    if x_parse_rest_api_key != API_KEY:
        return False
    return True


def create_jwt():
    """create jwt token"""
    payload = {"key": "ANY"}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token
