from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def pet_hello():
     return {"message":"pet_triage is reviewd"}



class ChatRequest(BaseModel):
     message: str
     sessionID: int

@app.post("/api/chat/message")
def chat(req: ChatRequest):
     return {"received":req.message, "sessionID": req.sessionID}