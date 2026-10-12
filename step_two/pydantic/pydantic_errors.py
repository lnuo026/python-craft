from pydantic import BaseModel, ValidationError

class Pet(BaseModel):
     name: str
     age: int

try:
     Pet(name="rex", age="abc")
except ValidationError as e:
     print(e)

try: 
     Pet(name="rex")
except ValidationError as e:
     print(e)