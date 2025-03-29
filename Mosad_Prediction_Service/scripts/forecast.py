import pandas as pd
from prophet import Prophet
import sys
import os
import pickle


def load_model(product_id):
    model_path = f"models/product_{product_id}_model.pkl"
    if not os.path.exists(model_path):
        print(f"Model not found for product_id {product_id}. Please train it first.")
        return None
    with open(model_path, "rb") as f:
        return pickle.load(f)


def forecast_product(product_id, periods=30):
    df = pd.read_csv(f"data/processed/product_{product_id}.csv")
    model = load_model(product_id)
    if model is None:
        return

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    forecast_dir = "data/forecasts"
    os.makedirs(forecast_dir, exist_ok=True)
    forecast_path = f"{forecast_dir}/forecast_{product_id}.csv"
    forecast.to_csv(forecast_path, index=False)
    print(f"Forecast saved to {forecast_path}")
    return forecast


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python forecast.py <product_id>")
        sys.exit(1)
    forecast_product(int(sys.argv[1]))
