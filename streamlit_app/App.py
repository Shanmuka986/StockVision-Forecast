"""
app.py

Landing Dashboard
StockVision Forecast V2
"""
import sys
import streamlit as st
from pathlib import Path
import pandas as pd

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

# ==========================================================
# Make Project Root Importable
# ==========================================================

if str(PROJECT_ROOT.parent) not in sys.path:

    sys.path.insert(
        0,
        str(PROJECT_ROOT.parent)
    )

# ==========================================================
# Startup
# ==========================================================

from src.startup import initialize_app
from streamlit_app.theme import render_theme_controls

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="StockVision Forecast V2",

    page_icon="📈",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Application Startup
# ==========================================================

initialize_app()

css_file = PROJECT_ROOT / "assets" / "styles.css"

if css_file.exists():

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    render_theme_controls()

    st.title("📈 StockVision")

    st.caption("Forecast V2")

    st.divider()

    st.subheader("🤖 Model")

    st.success("Linear Regression")

    st.divider()

    st.subheader("📊 Dataset")

    st.write("✅ 472 Companies")

    st.write("✅ Live Yahoo Finance")

    st.write("✅ Daily Predictions")

    st.write("✅ Prediction History")

    st.divider()

    st.subheader("🛠 Technology")

    st.write("• Python")

    st.write("• Pandas")

    st.write("• Scikit-Learn")

    st.write("• Streamlit")

    st.write("• yFinance")

# ==========================================================
# HERO SECTION
# ==========================================================

st.title("📈 StockVision Forecast V2")

st.markdown(
"""
### AI-Powered Stock Market Forecasting Platform

Predict the **next trading day's closing price**
using a Machine Learning model trained on historical
stock market data and powered by **live Yahoo Finance data**.

The application combines automated feature engineering,
real-time data acquisition, prediction history tracking,
and automatic prediction verification in a production-style
workflow.
"""
)

st.success(
"""


✔ Live Data
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ 472 Companies
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Automatic Verification
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Prediction History
"""
)

st.divider()
# ==========================================================
# QUICK STATISTICS
# ==========================================================

st.header("📊 Quick Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "🏢 Supported Companies",

        "472"

    )

with col2:

    st.metric(

        "🤖 ML Model",

        "Linear Regression"

    )

with col3:

    st.metric(

        "🎯 Prediction Target",

        "Next Trading Day"

    )

with col4:

    st.metric(

        "🌐 Data Source",

        "Yahoo Finance"

    )

st.divider()

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.header("🤖 Model Performance")

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.metric(

        "Prediction Accuracy*",

        "98.62%"

    )

with m2:

    st.metric(

        "R² Score",

        "0.9995"

    )

with m3:

    st.metric(

        "MAE",

        "$2.34"

    )

with m4:

    st.metric(

        "RMSE",

        "$5.97"

    )

# ==========================================================
# Learn About Model Metrics
# ==========================================================

with st.expander(
    "📚 Learn About Model Performance Metrics"
):

    st.markdown(
"""
### 🎯 Prediction Accuracy (98.62%)

Regression models do **not** have a built-in accuracy metric like
classification models.

For easier interpretation, Prediction Accuracy is derived using:

**Accuracy = (1 − MAPE) × 100**

A value of **98.62%** indicates that the model's average prediction
error is approximately **1.38%**.
"""
    )

    st.divider()

    st.markdown(
"""
### 📈 R² Score (0.9995)

The R² Score measures how well the model explains the variation
in stock prices.

- **Range:** 0 to 1
- **Closer to 1 = Better**

An R² Score of **0.9995** means the model explains approximately
**99.95% of the variance** in the target variable.
"""
    )

    st.divider()

    st.markdown(
"""
### 💵 MAE (Mean Absolute Error)

MAE measures the average absolute difference between the predicted
price and the actual closing price.

**MAE = 2.34 USD**

This means the prediction differs from the actual closing price by
approximately **$2.34** on average.
"""
    )

    st.divider()

    st.markdown(
"""
### 📉 RMSE (Root Mean Squared Error)

RMSE penalizes larger prediction errors more heavily than MAE.

**RMSE = 5.97 USD**

A relatively low RMSE indicates that the model produces very few
large prediction errors.
"""
    )

    st.divider()

    st.markdown(
"""
### 📊 MAPE (Mean Absolute Percentage Error)

MAPE measures prediction error as a percentage.

**MAPE = 1.38%**

A lower MAPE indicates better prediction performance.

Prediction Accuracy displayed in this application is calculated
directly from this value.
"""
    )

st.divider()

# ==========================================================
# WHY STOCKVISION?
# ==========================================================

st.header("🚀 Why StockVision?")

c1, c2 = st.columns(2)

with c1:

    st.success(
"""
⚡ **Live Yahoo Finance Integration**

Automatically downloads the latest
market data before every prediction.
"""
    )

    st.success(
"""
📊 **Prediction History**

Every prediction is automatically
stored for future verification.
"""
    )

with c2:

    st.success(
"""
🤖 **Machine Learning Forecasting**

Uses a trained Linear Regression
model with technical indicators.
"""
    )

    st.success(
"""
✅ **Automatic Prediction Verification**

Pending predictions are automatically
verified when the next trading day's
market data becomes available.
"""
    )

st.divider()

# ==========================================================
# LIVE PROJECT STATS
# ==========================================================

st.header("📌 Current Project Statistics")

history_file = PROJECT_ROOT.parent / "reports" / "prediction_history.csv"

if history_file.exists():

    history = pd.read_csv(history_file)

    total_predictions = len(history)

    pending = 0

    verified = 0

    if "Prediction Status" in history.columns:

        pending = len(
            history[
                history["Prediction Status"] == "Pending"
            ]
        )

        verified = len(
            history[
                history["Prediction Status"] == "Verified"
            ]
        )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Predictions",
        total_predictions
    )

    c2.metric(
        "Pending",
        pending
    )

    c3.metric(
        "Verified",
        verified
    )

else:

    st.info(
        "No prediction history available yet."
    )

st.divider()

# ==========================================================
# MACHINE LEARNING WORKFLOW
# ==========================================================

st.header("🧠 Prediction Workflow")

st.code(
"""
Live Yahoo Finance Data
          │
          ▼
Download Latest Stock Data
          │
          ▼
Feature Engineering
(Technical Indicators)
          │
          ▼
Linear Regression Model
          │
          ▼
Predict Next Trading Day
Closing Price
          │
          ▼
Store Prediction History
(CSV)
          │
          ▼
Automatic Prediction
Verification
""",
language="text"
)

st.caption(
"""
This workflow is executed automatically every time a prediction is generated.
"""
)

st.divider()

# ==========================================================
# APPLICATION PAGES
# ==========================================================

st.header("🚀 Application Modules")

m1, m2 = st.columns(2)

with m1:

    st.info(
"""
🏠 Home

Predict tomorrow's stock
closing price.
"""
    )

    st.info(
"""
📊 Prediction History

View all previous
predictions.
"""
    )

with m2:

    st.info(
"""
📁 Live Data

Browse downloaded
Yahoo Finance data.
"""
    )

    st.info(
"""
ℹ️ About

Learn about the project,
dataset and ML pipeline.
"""
    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

footer1, footer2, footer3 = st.columns(3)

with footer1:

    st.caption(
"""
**Application**

StockVision Forecast V2
"""
    )

with footer2:

    st.caption(
"""
**Machine Learning Model**

Linear Regression
"""
    )

with footer3:

    st.caption(
"""
**Data Source**

Yahoo Finance
"""
    )

st.divider()

st.caption(
"""
© 2026 StockVision Forecast V2

A production-style Machine Learning application developed for
next trading day stock price forecasting using Python,
Scikit-Learn, Pandas and Streamlit.
"""
)