from fastapi import FastAPI, HTTPException
from app.api import forecast

app = FastAPI(title="MOSAD-ML Forecasting API")

# Include the forecast routes
app.include_router(forecast.router)

@app.get("/")
def root():
    return {"message": "MOSAD-ML microservice is running!"}