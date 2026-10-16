# 这个文件自己运行没有任何输出,因为它只是定义了应用,没有谁去监听网络。要让它真正接收请求,得靠 uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

appTest = FastAPI()

@appTest.get("/")
def read_root():
     return {"status": "Hammer"}

class Pet(BaseModel):
     name: str
     age: int

@appTest.post("/pets")
# 函数的参数 pet,类型写成 Pet,这一句告诉 FastAPI"请求体应该符合 Pet 的格式"
def create_pet(pet: Pet):
     print("create_pet is executing")
     return {"name": pet.name, "age_next_year": pet.age+1}


