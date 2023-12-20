from fastapi import status
from sqlalchemy.orm import Session

from main import app
from schemas import Archive_request
from db.db_helpers import get_db
import db.repository as handlers
from db.repository import archive

@app.get("/")
def root():
    return "archive"

@app.post("/archive", status_code=status.HTTP_201_CREATED)
def create_archive(archive: Archive_request, db:Session):
    return handlers.archive(archive, db)

@app.get("/archive/{id}")
def read_archive(id: int, db:Session):
        return f"read archive item with id: {handlers.archive.id} and year: {handlers.archive.year}"

@app.put("/archive/{id}")
def update_archive(id: int):
    return "update archive item with id {id}"

@app.delete("/archive/{id}")
def delete_archive(id: int):
    return "delete archive item with id {id}"

@app.get("/archive")
def read_archive_list():
    return "read archive list"