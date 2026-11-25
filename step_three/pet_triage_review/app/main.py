from fastapi import FastAPI
from pydantic import BaseModel
from services.session import add_message, get_history, make_message
from services.triage import parse_triage
from services.gemini import call_gemini

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
     history = get_history(req.sessionID)
     user_message = make_message("user", req.message)
     contents = history + [user_message]

     # return {"triage_level": level, "clean_text": clean_text}
     raw = call_gemini(contents)
     parse = parse_triage(raw)
     
     
     add_message(req.sessionID, "user", req.message)
     add_message(req.sessionID, "model", raw)

     
     history = get_history(req.sessionID)
     return {"sessionID":req.sessionID, 
             "messageCount":len(history),
             "get_history":get_history(req.sessionID),
             "triageLevel": parse["triage_level"],
             "reply": parse["clean_text"]}

