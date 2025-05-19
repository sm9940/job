from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import Test
app = FastAPI()
engine = engineconn()
session = engine.sessionmaker()
tables = engine.create_tables()
class Item(BaseModel):
    name : str
    number : int
@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example