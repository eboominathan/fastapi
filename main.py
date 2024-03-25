from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def index():
        return {"msg":"Hello Boomi"}
    
@app.get("/about")
def about():
        return {"msg":"Hello about"}
    
@app.get("/user/{id}")
def user(id:int,limit:Optional[int]=None):
    if limit is None:    
         return {"data":id}
    else:
         return {"data":{"id":id,"limit":limit}}
