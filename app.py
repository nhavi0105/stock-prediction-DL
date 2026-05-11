from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

app = FastAPI()

model = tf.keras.models.load_model("lstm_model.h5")

class StockInput(BaseModel):
    stock: str

STOCK_FILES = {
    "AAPL": "sample_data/AAPL.csv",
    "ACG": "sample_data/ACG-VNINDEX-History.csv",
    "ADP": "sample_data/ADP-UpcomIndex-History.csv",
}

def predict_return_and_volatility(file_path):
    df = pd.read_csv(file_path)

    # ===== FIX DATE =====
    if 'TradingDate' in df.columns:
        df['Date'] = pd.to_datetime(df['TradingDate'])
    elif 'Date' in df.columns:
        df['