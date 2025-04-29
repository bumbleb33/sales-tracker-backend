from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum  # <-- Needed for Vercel serverless

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse({"message": "Sales Tracker API running!"})

handler = Mangum(app)  # <-- Important for serverless
