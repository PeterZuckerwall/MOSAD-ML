from fastapi import APIRouter, Path, HTTPException
from app.services.prophet_service import run_forecast_pipeline

router = APIRouter(prefix="/forecast", tags=["Forecasting"])

@router.get("/{product_id}")
def forecast_product(product_id: int):
    result = run_forecast_pipeline(product_id)
    if result is None:
        raise HTTPException(status_code=404, detail="No data found or forecast failed")
    return result
