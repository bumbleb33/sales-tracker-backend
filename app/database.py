from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

DATABASE_URL = "postgresql://sales_backend_user:ootonymGVB9WBTnjwpJPYgQVFn0ZT2z0@dpg-d08j0geuk2gs73bc00ig-a/sales_backend"

# Only use connect_args if SQLite
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def create_db_and_tables():
    from app import models
    Base.metadata.create_all(bind=engine)
