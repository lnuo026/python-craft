# 这个文件自己运行没有任何输出,因为它只是定义了应用,没有谁去监听网络。要让它真正接收请求,得靠 uvicorn
from fastapi import FastAPI

appTest = FastAPI()

@appTest.get("/")
def read_root():
     return {"status": "ok"}