from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql://sales_backend_user:ootonymGVB9WBTnjwpJPYgQVFn0ZT2z0@dpg-d08j0geuk2gs73bc00ig-a/sales_backend"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    executive_name = Column(String)
    model = Column(String)
    amount_collected = Column(Float)
    region = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
