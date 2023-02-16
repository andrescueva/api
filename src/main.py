
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
app = FastAPI()


class Message(BaseModel):
    message: str
    to: str
    from_: str = Field(...,alias="from")
    timeToLifeSec: int


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
