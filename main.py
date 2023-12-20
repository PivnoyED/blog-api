
from fastapi import FastAPI, status

from db.model import Base
from db.db_helpers import engine

        
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return "archive"

@app.post("/archive", status_code=status.HTTP_201_CREATED)
def create_archive():
    return "create archive item"

@app.get("/archive/{id}")
def read_archive(id: int):
    return "read archive item with id {id}"

@app.put("/archive/{id}")
def update_archive(id: int):
    return "update archive item with id {id}"

@app.delete("/archive/{id}")
def delete_archive(id: int):
    return "delete archive item with id {id}"

@app.get("/archive")
def read_archive_list():
    return "read archive list"
