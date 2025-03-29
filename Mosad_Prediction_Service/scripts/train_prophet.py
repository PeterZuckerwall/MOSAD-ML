import pandas as pd
from prophet import Prophet
import sys
import os


def train_prophet_model(product_id, periods=30):
    file_path = f"data/processed/product_{product_id}.csv"
    if not os.path.exists(file_path):
        print(f"Data file not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    model = Prophet()
    model.fit(df)

    model_dir = "models"
    os.makedirs(model_dir, exist_ok=True)
    model_path = f"{model_dir}/product_{product_id}_model.pkl"
    with open(model_path, "wb") as f:
        import pickle
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")
    return model


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train_prophet.py <product_id>")
        sys.exit(1)
    train_prophet_model(int(sys.argv[1]))
