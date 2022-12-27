from fastapi import FastAPI
from pydantic import BaseModel
import pickle
#import app.items as items

class VarItem(BaseModel):
    name: str
    description: str | None = None
    value: float

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getVars/{item}")
async def read_item(item):
    file = open(item, 'rb')
    i = pickle.load(file)
    file.close()
    return {"Value": i.value}


@app.post("/postVars/")
async def create_item(Item: VarItem):
    file = open(Item.name, 'wb')
    pickle.dump(Item,file)
    file.close()
    return Item.__dict__