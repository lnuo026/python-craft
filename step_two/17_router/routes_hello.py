from fastapi import APIRouter

routerTest = APIRouter()

@routerTest.get("/hello")
def say_hello():
     return {"message": "hello from the router"}