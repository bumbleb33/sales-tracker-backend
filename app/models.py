from sqlalchemy import Column, Integer, String, Date, Float
from app.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    executive_name = Column(String)
    model = Column(String)
    amount_collected = Column(Float)
    region = Column(String)
    date = Column(Date)
    units_sold = Column(Integer, default=1)


class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String)
    target_type = Column(String)  # 'daily' or 'monthly'
    target_devices = Column(Integer)
    deadline = Column(Date)

class Incentive(Base):
    __tablename__ = "incentives"
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String)
    milestone_devices = Column(Integer)
    reward = Column(String)
