from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.routers import sales, admin

app = FastAPI()

origins = ["*"]  # Update this with your frontend URL for production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(sales.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Sales Tracker Backend: Sales + Admin API"}
