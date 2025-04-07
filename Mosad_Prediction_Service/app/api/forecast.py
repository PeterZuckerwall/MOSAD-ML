from fastapi import APIRouter
from app.services.forecast_service import get_tyre_forecast_from_csv, get_tube_forecast_from_csv, get_revenue_forecast_from_csv
from typing import List, Dict, Any

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/tyres", response_model=List[Dict[str, Any]])
async def forecast_tyres():
    return get_tyre_forecast_from_csv()

@router.get("/tubes", response_model=List[Dict[str, Any]])
async def forecast_tubes():
    return get_tube_forecast_from_csv()

@router.get("/revenue", response_model=List[Dict[str, Any]])
async def forecast_revenue():
    return get_revenue_forecast_from_csv()