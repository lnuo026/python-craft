from fastapi import FastAPI
from routes_hello import routerTest

app = FastAPI()
app.include_router(routerTest) 

@app.get("/")
def main():
     return {"page": "home"}