
import pandas as pd
import os

def preprocess_sales_data(raw_csv_path):
    # Load raw sales data
    df = pd.read_csv(raw_csv_path)

    # Drop unnecessary columns
    df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col], errors='ignore')

    # Rename columns for consistency
    df.columns = ['sale_date', 'product_category', 'product_size', 'brand', 'quantity_sold', 'total_price']

    # Convert sale_date to datetime
    df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

    # Clean and convert total_price
    df['total_price'] = pd.to_numeric(df['total_price'], errors='coerce')

    # Fill NaNs and convert quantity_sold to integer
    df['quantity_sold'] = df['quantity_sold'].fillna(0).astype(int)

    # Drop rows with missing sale_date
    df = df.dropna(subset=['sale_date'])

    # Split datasets
    df_tyres = df[df['product_category'].str.lower() == 'tyre']
    df_tubes = df[df['product_category'].str.lower() == 'tube']

    # Group by sale_date for stock predictions
    df_tyres_stock = df_tyres.groupby('sale_date', as_index=False)['quantity_sold'].sum()
    df_tyres_stock.columns = ['ds', 'y']

    df_tubes_stock = df_tubes.groupby('sale_date', as_index=False)['quantity_sold'].sum()
    df_tubes_stock.columns = ['ds', 'y']

    # Group by sale_date for revenue predictions
    df_revenue = df.groupby('sale_date', as_index=False)['total_price'].sum()
    df_revenue.columns = ['ds', 'y']

    # Save processed datasets
    os.makedirs('data/processed', exist_ok=True)
    df_tyres_stock.to_csv('data/processed/tyre_stock.csv', index=False)
    df_tubes_stock.to_csv('data/processed/tube_stock.csv', index=False)
    df_revenue.to_csv('data/processed/revenue.csv', index=False)

    print("✅ Data preprocessing complete. Processed files saved in data/processed/.")


if __name__ == "__main__":
    raw_csv_path = "data/raw/MOSAD_sales_history.csv"
    preprocess_sales_data(raw_csv_path)
