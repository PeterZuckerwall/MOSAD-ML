
import pandas as pd
from prophet import Prophet
import os
import pickle

def train_and_save_model(data_path, model_save_path, model_name):
    # Load processed data
    df = pd.read_csv(data_path)

    # Initialize and fit Prophet model
    model = Prophet()
    model.fit(df)

    # Save the model
    os.makedirs(model_save_path, exist_ok=True)
    model_file = os.path.join(model_save_path, f"{model_name}.pkl")
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

    print(f"✅ Trained and saved {model_name} model at {model_file}")

if __name__ == "__main__":
    # Define paths
    processed_dir = "data/processed"
    models_dir = "models"

    # Training Tyre Stock Model
    train_and_save_model(
        data_path=os.path.join(processed_dir, "tyre_stock.csv"),
        model_save_path=models_dir,
        model_name="tyre_stock_model"
    )

    # Training Tube Stock Model
    train_and_save_model(
        data_path=os.path.join(processed_dir, "tube_stock.csv"),
        model_save_path=models_dir,
        model_name="tube_stock_model"
    )

    # Training Revenue Model
    train_and_save_model(
        data_path=os.path.join(processed_dir, "revenue.csv"),
        model_save_path=models_dir,
        model_name="revenue_model"
    )
