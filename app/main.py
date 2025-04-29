from fastapi import FastAPI
from app.routers import users, sales, leads

app = FastAPI(title="Sales Tracker API")

app.include_router(users.router)
app.include_router(sales.router)
app.include_router(leads.router)
