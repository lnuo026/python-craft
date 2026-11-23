from fastapi import FastAPI
from pydantic import BaseModel
from services.session import add_message, get_history

app = FastAPI()

@app.get("/")
def pet_hello():
     return {"message":"pet_triage is reviewd"}



class ChatRequest(BaseModel):
     message: str
     sessionID: int

# 先存，再读，最后数。
@app.post("/api/chat/message")
def chat(req: ChatRequest):
     add_message(req.sessionID, "user", req.message)
     history = get_history(req.sessionID)
     return {"sessionID":req.sessionID, "messageCount":len(history)}

