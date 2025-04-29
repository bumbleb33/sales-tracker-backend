from fastapi import APIRouter

router = APIRouter()

@router.get("/sales")
def get_sales():
    return {"msg": "List of sales"}
