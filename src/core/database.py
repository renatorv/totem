from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATA_BASE = "postgresql://postgres:159753@localhost:5432/postgres"

engine = create_engine(DATA_BASE, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

GetDBDep = Annotated[Session, Depends(get_db)]