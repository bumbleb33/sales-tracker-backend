from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"message": "Sales Tracker API running via Vercel!"})

handler = Mangum(app)
