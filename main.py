from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.routers import admin

app = FastAPI()

# CORS for frontend connection
origins = ["*"]  # Replace with your Vercel domain in production

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

# Include routers
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Sales Tracker Backend with Targets & Incentives"}
