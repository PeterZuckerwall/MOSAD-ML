import pandas as pd
import os

def load_forecast_csv(file_path):
    df = pd.read_csv(file_path)
    forecast = df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    return forecast.to_dict(orient="records")

def get_tyre_forecast_from_csv():
    file_path = "data/forecasts/2020_December_tyre_forecast.csv"
    return load_forecast_csv(file_path)

def get_tube_forecast_from_csv():
    file_path = "data/forecasts/2020_December_tube_forecast.csv"
    return load_forecast_csv(file_path)

def get_revenue_forecast_from_csv():
    file_path = "data/forecasts/2020_October_revenue_forecast.csv"
    return load_forecast_csv(file_path)
