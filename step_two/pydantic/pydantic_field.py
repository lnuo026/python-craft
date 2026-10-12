from pydantic import BaseModel, Field, ValidationError

class ChatRequest(BaseModel):
     message: str = Field(..., max_length=6)
     sessionId: str

ok = ChatRequest(message="my dog", sessionId="s1")
print(ok)

try:
     ChatRequest(message="my dog is very sick today", sessionId="s2")
except ValidationError as e:
     print(e)


class Response(BaseModel):
     history: str = Field("I say", max_length=10)
     sessionId: str

user = Response(sessionId="s3")
print(user)