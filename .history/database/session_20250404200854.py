from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = ""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread":False}
)

SesionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db() -> Generator
try:
    db = SessionLocal()
    yield db

finally:
    db.close()