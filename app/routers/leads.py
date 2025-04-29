from fastapi import APIRouter

router = APIRouter()

@router.get("/leads")
def get_leads():
    return {"msg": "List of leads"}
