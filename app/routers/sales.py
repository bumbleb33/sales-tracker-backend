from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, Sale

router = APIRouter(prefix="/sales", tags=["Sales"])

class SaleCreate(BaseModel):
    executive_name: str
    model: str
    amount_collected: float
    region: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    new_sale = Sale(**sale.dict())
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale

@router.get("/")
def get_sales(db: Session = Depends(get_db)):
    return db.query(Sale).all()
