import pandas as pd
import requests
import time
from datetime import datetime

API_URL = "http://127.0.0.1:8000/predict_stock"

STOCKS = ["AAPL", "ACG", "ADP"]

OUTPUT_FILE = "prediction_results.csv"


def call_model(stock):
    try:
        response = requests.post(
            API_URL,
            json={"stock": stock}
        )
        data = response.json()

        if "error" in data:
            print(f"Error with {stock}: {data['error']}")
            return None

        return data

    except Exception as e:
        print(f"API error for {stock}: {e}")
        return None


def run_pipeline():
    print("Running pipeline...")

    results = []

    for stock in STOCKS:
        print(f"Processing {stock}...")

        result = call_model(stock)

        if result:
            result["timestamp"] = datetime.now()
            results.append(result)

    if len(results) == 0:
        print("No data collected")
        return

    df = pd.DataFrame(results)

    print("\n Result:")
    print(df)

    try:
        from db import save_to_db

        save_to_db(df)
        print("Saved to database (stock.db)")
        print(f"Saved to {OUTPUT_FILE}")
    except Exception as e:
        print("Error saving file:", e)

def run_every(interval_seconds=60):
    while True:
        run_pipeline()
        print(f"Waiting {interval_seconds} seconds...\n")
        time.sleep(interval_seconds)

# MAIN
if __name__ == "__main__":
    run_pipeline()
