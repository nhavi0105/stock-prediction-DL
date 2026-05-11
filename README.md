## 1. Project Overview
This project presents an end-to-end machine learning system for stock price prediction and decision support.

The system uses an LSTM (Long Short-Term Memory) model to analyze historical stock data and predict future price trends. Based on predicted return and market volatility, the system provides investment recommendations (BUY or AVOID).

The project demonstrates a complete pipeline from:
- Data processing
- Model training
- Model deployment (SaaS)
- Dashboard visualization
- Automation workflow


## 2. Repository Structure

The repository is organized as follows:

stock-prediction-DL/ │ ├── app.py # FastAPI backend (model serving) ├── app_ui.py # Streamlit dashboard (UI) ├── pipeline.py # Automation pipeline (Task 5.3) ├── db.py # SQLite database utilities ├── sample_data/ # Datasets used  ├── Final-project-DL4AI.ipynb # Model training notebook ├── README.md

## 3. Key Features

- Time-series forecasting using LSTM
- Stock return prediction
- Volatility-based risk scoring
- Investment decision system (Buy / Avoid)
- REST API deployment (FastAPI)
- Interactive dashboard (Streamlit)
- Automated pipeline (data → model → database)

## 4. System Architecture

The system consists of three main components:

1. **Model Layer**
   - LSTM model trained in notebook
   - Saved and loaded in `app.py`

2. **Backend (SaaS API)**
   - FastAPI serves prediction endpoint `/predict_stock`
   - Accepts stock symbol → returns prediction + risk

3. **Frontend (Dashboard)**
   - Streamlit UI displays:
     - Table
     - Return chart
     - Risk chart

4. **Automation Layer (Task 5.3)**
   - `pipeline.py` automatically:
     - Calls API
     - Stores results in SQLite
   - Dashboard reads from database

## 5. Installation & Setup

### 5.1 Clone repository

```bash
git clone https://github.com/nhavi0105/stock-prediction-DL.git
cd stock-prediction-DL

###  5.2 Install dependencies
pip install -r requirements.txt

## 6. How to Run the System
Step 1 — Run Backend API
uvicorn app:app --reload
API will run at:
http://127.0.0.1:8000

Step 2 — Run Streamlit Dashboard
streamlit run app_ui.py
Dashboard will run at:
http://localhost:8501

Step 3 — Run Automation Pipeline (Task 5.3)
python pipeline.py
This will:
Call the API
Generate predictions
Save results into SQLite database

## 7. Output Description
The system produces:
Return (%) → expected profit/loss
Volatility → market risk
Risk Score → combined risk metric
Decision:
BUY (low risk)
AVOID (high risk)
Displayed in:
Table (decision highlighted)
Bar charts (green/red for return)

## 8. Reproducibility Notes
Due to file size limitations, the following are excluded:
Trained model (.h5)
Database (.db)
Full dataset
To reproduce results:
Run the notebook to train model
Run pipeline.py to generate predictions
Launch dashboard

## 9. Commit History
The repository includes meaningful commits reflecting development stages:
Model development (notebook)
Backend API implementation
UI dashboard creation
Pipeline automation
Database integration

## 10. Future Improvements
Integrate real-time stock data APIs
Improve model accuracy (Transformer / Attention models)
Deploy to cloud (AWS / GCP)
Enhance risk modeling


