from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Target, Incentive
from app.schemas import TargetCreate, IncentiveCreate

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/targets")
def create_target(target: TargetCreate, db: Session = Depends(get_db)):
    new_target = Target(**target.dict())
    db.add(new_target)
    db.commit()
    db.refresh(new_target)
    return new_target

@router.get("/targets")
def get_targets(db: Session = Depends(get_db)):
    return db.query(Target).all()

@router.post("/incentives")
def create_incentive(incentive: IncentiveCreate, db: Session = Depends(get_db)):
    new_incentive = Incentive(**incentive.dict())
    db.add(new_incentive)
    db.commit()
    db.refresh(new_incentive)
    return new_incentive

@router.get("/incentives")
def get_incentives(db: Session = Depends(get_db)):
    return db.query(Incentive).all()
