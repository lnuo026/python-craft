from pydantic import BaseModel

class Pet(BaseModel):
     name: str
     age: int


real_pet = Pet(name="Rex", age=4)
false_pet = Pet(name="wrong", age="4")
print(real_pet)
print(real_pet.name, real_pet.age)

print(false_pet)
print(false_pet.name, false_pet.age)
