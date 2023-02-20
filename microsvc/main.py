from fastapi import FastAPI, Depends
from starlette.exceptions import HTTPException
from microsvc.models import Message

from microsvc.dependencies import validate_api_key, create_jwt


app = FastAPI()


@app.post("/DevOps/")
async def send_message(

    message: Message, x_parse_rest_api_key: str = Depends(validate_api_key)
):
    """Post message protected with api key"""
    message_dict = message.dict()
    to = message_dict["to"]
    return {"message": f"Hello {to} your message will be send"}


@app.get("/DevOps/")
async def get_send_message():
    """Method get not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.delete("/DevOps/")
async def delete_send_message():
    """Method deleye not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.put("/DevOps/")
async def put_send_message():
    """Method put not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.patch("/DevOps/")
async def patch_send_message():
    """Method patch not allowed"""
    raise HTTPException(status_code=405, detail="ERROR")


@app.get("/jwt/")
async def get_token(token: str = Depends(create_jwt)):
    """endpoint to get token"""
    return {"token": token}


@app.get("/health/")
async def get_health_status():
    """health status check endpoint"""
    return {"status": "OK80"}
