from pydantic import BaseModel
from datetime import date

class SaleCreate(BaseModel):
    executive_name: str
    model: str
    amount_collected: float
    region: str
    units_sold: int = 1


class TargetCreate(BaseModel):
    region: str
    target_type: str
    target_devices: int
    deadline: date

class IncentiveCreate(BaseModel):
    region: str
    milestone_devices: int
    reward: str
