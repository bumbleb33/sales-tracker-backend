from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sales
from app.database import create_db_and_tables

app = FastAPI()

# --- ADD THIS CORS SETUP ---
origins = [
    "https://tracker-git-master-bumblebs-projects.vercel.app",
    "http://localhost:5173"  # also allow local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- END CORS SETUP ---

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
