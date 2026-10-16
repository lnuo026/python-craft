from fastapi import APIRouter
from pydantic import BaseModel

# router = APIRouter() 是新的迷你表,以及装饰器从 @appTest.post 换成了 @router.post
router = APIRouter()

class Pet(BaseModel):
     name: str
     age:int

@router.post('/pets')
def create_pet(pet: Pet):
     print("create_pet is executing")
     return{"name": pet.name, "age_next_year": pet.age+1}


