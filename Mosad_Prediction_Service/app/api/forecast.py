from fastapi import APIRouter
from fastapi import Response
from fastapi.responses import FileResponse
from app.services.forecast_service import get_tyre_forecast_from_csv, get_tube_forecast_from_csv, get_revenue_forecast_from_csv
from typing import List, Dict, Any
import os

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/download/tyre-forecast")
async def download_tyre_forecast():
    file_path = "data/forecasts/2020_September_tyre_forecast.csv"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="tyre_forecast.csv", media_type='text/csv')
    else:
        return Response(content="Tyre forecast file not found.", status_code=404)

@router.get("/download/tube-forecast")
async def download_tube_forecast():
    file_path = "data/forecasts/2020_September_tube_forecast.csv"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="tube_forecast.csv", media_type='text/csv')
    else:
        return Response(content="Tube forecast file not found.", status_code=404)


@router.get("/revenue", response_model=List[Dict[str, Any]])
async def forecast_revenue():
    return get_revenue_forecast_from_csv()

@router.get("/download/revenue-forecast")
async def download_revenue_forecast():
    file_path = "data/forecasts/2020_October_revenue_forecast.csv"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="sales_revenue_forecast.csv", media_type='text/csv')
    else:
        return Response(content="Revenue forecast file not found.", status_code=404)

@router.get("/tyres-json")
async def get_tyre_forecast_json():
    file_path = "data/forecasts/tyre_forecast.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df_selected = df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        return df_selected.to_dict(orient="records")
    else:
        return Response(content="Tyre forecast file not found.", status_code=404)
