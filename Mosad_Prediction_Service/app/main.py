from fastapi import FastAPI
from app.api import forecast

app = FastAPI(title="MOSAD-ML Prediction Service")


app.include_router(forecast.router)

@app.get("/")
async def root():
    return {"message": "MOSAD-ML microservice is running!"}