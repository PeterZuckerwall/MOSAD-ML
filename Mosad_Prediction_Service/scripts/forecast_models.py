
import pandas as pd
from prophet import Prophet
import os
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def generate_forecast(model, periods=30):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def forecast_and_save(model_path, forecast_save_path, forecast_name, periods=30):
    model = load_model(model_path)
    forecast = generate_forecast(model, periods)

    os.makedirs(forecast_save_path, exist_ok=True)
    forecast_file = os.path.join(forecast_save_path, f"{forecast_name}.csv")
    forecast.to_csv(forecast_file, index=False)

    print(f"✅ Forecast saved: {forecast_file}")

if __name__ == "__main__":
    models_dir = "models"
    forecasts_dir = "data/forecasts"

    # Forecast Tyre Stock
    forecast_and_save(
        model_path=os.path.join(models_dir, "tyre_stock_model.pkl"),
        forecast_save_path=forecasts_dir,
        forecast_name="tyre_forecast",
        periods=30
    )

    # Forecast Tube Stock
    forecast_and_save(
        model_path=os.path.join(models_dir, "tube_stock_model.pkl"),
        forecast_save_path=forecasts_dir,
        forecast_name="tube_forecast",
        periods=30
    )

    # Forecast Revenue
    forecast_and_save(
        model_path=os.path.join(models_dir, "revenue_model.pkl"),
        forecast_save_path=forecasts_dir,
        forecast_name="revenue_forecast",
        periods=30
    )
