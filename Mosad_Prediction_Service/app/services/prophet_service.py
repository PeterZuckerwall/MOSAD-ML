from scripts.fetch_sales import fetch_sales_by_product
from scripts.train_prophet import train_prophet_model
from scripts.forecast import forecast_product


def run_forecast_pipeline(product_id: int, periods: int = 30):
    df = fetch_sales_by_product(product_id)
    if df is None or df.empty:
        return None

    train_prophet_model(product_id)
    forecast_df = forecast_product(product_id, periods)

    if forecast_df is not None:
        return forecast_df.tail(periods).to_dict(orient="records")
    return None
