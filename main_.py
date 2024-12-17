from typing import Union
from fastapi import FastAPI, HTTPException
import db_utils
import helper

app = FastAPI()

@app.get("/")
def root():
    return "This is server's root."

@app.post("/post")
def get_post():
    return {"id": 0, "timestamp": 0}

@app.get("/dog")
def get_dogs(kind: str):
    helper.validate_kind(kind)

    return db_utils.get_dogs_by_kind(kind)

@app.post("/dog")
def create_dog(dog: db_utils.Dog):
    return "ok"

@app.get("/dog/{pk}")
def get_dog_by_pk(pk: str):
    return db_utils.generate_dog(pk=pk)

@app.patch("/dog/{pk}")
def update_dog(pk: str, dog: db_utils.Dog):
    return db_utils.generate_dog(pk=pk, name=dog.name, kind=dog.kind)