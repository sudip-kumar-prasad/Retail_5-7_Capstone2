import pandas as pd
import numpy as np
import os

def run_etl():
    print("Starting ETL pipeline...")
    
    # 1. Extract / Load Raw Data
    raw_data_path = "data/raw/superstore_raw.csv"
    if not os.path.exists(raw_data_path):
        # Fallback if running from within scripts/ directory
        raw_data_path = "../data/raw/superstore_raw.csv"
        
    df = pd.read_csv(raw_data_path, encoding='latin1')
    print(f"Data loaded successfully. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    # 2. Transform (Clean and Engineer Features)
    df = df.drop_duplicates()
    print("Duplicates removed.")
    
    df["Order.Date"] = pd.to_datetime(df["Order.Date"])
    df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])
    
    df["Month"] = df["Order.Date"].dt.month
    df["Month_Name"] = df["Order.Date"].dt.month_name()
    df["Day"] = df["Order.Date"].dt.day
    df["Shipping_Days"] = (df["Ship.Date"] - df["Order.Date"]).dt.days
    df["Profit_Margin_%"] = (df["Profit"] / df["Sales"]) * 100
    
    df.replace([np.inf, -np.inf], 0, inplace=True)
    print("Data transformed and new features engineered.")
    
    # 3. Load (Export Processed Data)
    processed_data_path = "data/processed/superstore_cleaned.csv"
    if not os.path.exists(os.path.dirname(processed_data_path)):
        processed_data_path = "../data/processed/superstore_cleaned.csv"
        
    df.to_csv(processed_data_path, index=False)
    print(f"✅ Cleaning Completed Successfully. Saved to {processed_data_path}")

if __name__ == "__main__":
    run_etl()
