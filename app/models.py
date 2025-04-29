from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)  # 'executive', 'manager', 'admin'

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    executive_id = Column(Integer, ForeignKey("users.id"))
    model = Column(String)
    amount_collected = Column(Float)
    location = Column(String)
    capex_opex = Column(String)
    created_at = Column(DateTime, default=func.now())
