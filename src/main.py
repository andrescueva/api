
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Message(BaseModel):
    message: str
    to: str
    from_: str
    timeToLifeSec: int


@app.post("/DevOps/")
async def send_message(message: Message):
    message_dict = message.dict()
    to = message_dict['to']
    return {"message": f"Hello {to} your message will be send"}


