from fastapi import FastAPI
from app.routers import sales
from app.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(sales.router)

@app.get("/")
def root():
    return {"message": "Sales Tracker API running with Sales endpoint"}

@app.get("/routes")
def list_routes():
    return [route.path for route in app.router.routes]
