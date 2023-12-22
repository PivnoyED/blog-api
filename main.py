from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.model import Base
from db.db_helpers import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()