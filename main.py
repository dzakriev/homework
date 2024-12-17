
from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get("/")
def root():
    return "This is server's root."

@app.post("/post")
def get_post():
    return {"id": 0, "timestamp": 0}

@app.get("/dog")
def get_dogs(kind: DogType):
    return [dog for dog in dogs_db.values() if dog.kind == kind]

@app.post("/dog")
def create_dog(dog: Dog):
    if dogs_db.get(dog.pk) != None:
        raise HTTPException(status_code=422, detail="Pk already exists")
    
    dogs_db[dog.pk] = dog
    return dog

@app.get("/dog/{pk}")
def get_dog_by_pk(pk: int):
    return dogs_db.get(pk)

@app.patch("/dog/{pk}")
def update_dog(pk: int, dog: Dog):
    if dogs_db.get(dog.pk) == None:
        raise HTTPException(status_code=422, detail="Pk doesn't exists")
    
    if  pk != dog.pk:
        raise HTTPException(status_code=422, detail="Pk doesn't match request's body")
    
    dogs_db[pk] = dog
    return dog