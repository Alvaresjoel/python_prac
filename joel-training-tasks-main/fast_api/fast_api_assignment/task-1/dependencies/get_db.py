from typing import Annotated
from sqlalchemy.orm import Session,sessionmaker
from fastapi import Depends
from db import engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
