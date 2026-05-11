import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from db import load_latest

API_URL = "http://127.0.0.1:8000/predict_stock"

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("Stock Decision Dashboard")

mode = st.radio("Select Mode", ["Real-time (API)", "Batch (Database)"])

stocks = ["AAPL", "ACG", "ADP"]

if mode == "Real-time (API)":

    st.write("Using live API (FastAPI)")

    if st.button("Run Real-time Prediction"):

        results = []

        for stock in stocks:
            try:
                response = requests.post(
                    API_URL,
                    json={"stock": stock}
                )

                data = response.json()

                if "error" not in data:
                    results.append(data)

            except Exception as e:
                st.error(f"API error for {stock}: {e}")

        if len(results) == 0:
            st.warning("No data returned from API")
        els