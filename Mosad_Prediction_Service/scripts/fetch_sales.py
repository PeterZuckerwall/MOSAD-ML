
import pandas as pd
from sqlalchemy import create_engine
import yaml
import os

with open("config/db_config.yaml") as f:
    db_config = yaml.safe_load(f)

DB_URI = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(DB_URI)

def fetch_sales_by_product(product_id):
    query = f"""
    SELECT sale_date AS ds, quantity_sold AS y, product_size, brand
    FROM sales_history
    WHERE product_id = {product_id}
    ORDER BY sale_date;
    """
    df = pd.read_sql(query, engine)

    if df.empty:
        print(f"No sales data found for product_id={product_id}")
        return None

    filename = f"data/processed/product_{product_id}.csv"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Saved data for product_id={product_id} to {filename}")
    return df

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fetch_sales.py <product_id>")
        sys.exit(1)
    fetch_sales_by_product(int(sys.argv[1]))
