import pandas as pd
from prophet import Prophet
import os
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def forecast_future(model, last_history_date, periods=30):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    future_forecast = forecast[forecast['ds'] > last_history_date]
    return future_forecast

if __name__ == "__main__":
    model_path = "models/revenue_model.pkl"
    data_path = "data/processed/revenue.csv"
    forecast_dir = "data/forecasts"

    model = load_model(model_path)
    df_history = pd.read_csv(data_path)
    last_history_date = pd.to_datetime(df_history['ds']).max()

    forecast = forecast_future(model, last_history_date, periods=30)

    # Revenue is money, so we don't round it to whole numbers!

    # Get the forecast start month and year
    start_date = pd.to_datetime(forecast['ds'].min())
    year = start_date.year
    month = start_date.strftime('%B')

    filename = f"{year}_{month}_revenue_forecast.csv"
    forecast_save_path = os.path.join(forecast_dir, filename)

    os.makedirs(forecast_dir, exist_ok=True)
    forecast.to_csv(forecast_save_path, index=False)

    print(f"✅ Revenue forecast saved to {forecast_save_path}")
