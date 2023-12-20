from fastapi import FastAPI, status
from db.model import Base

from db.db_helpers import engine
    
# Создание базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI()