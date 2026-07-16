# 📈 StockVision Forecast V2

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

> **A Production-Ready Machine Learning Stock Forecasting Application**

Predict the **next trading day's closing price** of S&P 500 companies using Machine Learning, live Yahoo Finance data, technical indicators, and an interactive Streamlit dashboard.

---
## 🚀 Live Demo

- 🚀 **Live Demo:** https://stockvision-forecast.streamlit.app/
- 📂 **GitHub Repository:** https://github.com/Shanmuka986/StockVision-Forecast

---

## 🚀 Project Highlights

- 📊 Predicts the **Next Trading Day Closing Price**
- 📈 Uses **Live Yahoo Finance Market Data**
- 🤖 Machine Learning based on **Linear Regression**
- 📉 Technical Indicators (RSI, EMA, MACD, Bollinger Bands, Moving Averages)
- 🕒 Automatic Prediction Verification using actual market closing prices
- 📚 Prediction History Tracking
- 🎨 Modern Multi-Page Streamlit Dashboard
- ⚡ Smart Local Data Caching
- 🏗️ Modular Production-Style Project Structure

---

## 🎯 Project Objective

StockVision Forecast V2 was built to simulate a real-world machine learning application rather than a simple notebook-based prediction model.

The application downloads live market data, performs feature engineering, predicts the next trading day's closing price, stores every prediction, and automatically verifies prediction accuracy after the market closes.

The project follows industry best practices by separating data preprocessing, feature engineering, model training, prediction, verification, and user interface into independent modules.

---
# ✨ Features

## 🤖 Machine Learning

- Predicts the **next trading day's closing price**
- Trained using **Linear Regression**
- Uses chronological train-test split to avoid data leakage
- Automatically loads the best trained model
- Fast prediction with optimized preprocessing

---

## 📈 Live Market Data

- Downloads real-time stock data using **Yahoo Finance**
- Supports **472 S&P 500 companies**
- Automatically caches downloaded market data
- Prevents unnecessary API requests
- Refreshes data whenever required

---

## 📊 Technical Indicators

The prediction model uses multiple technical indicators, including:

- Relative Strength Index (RSI)
- Exponential Moving Average (EMA)
- Moving Averages (5, 10, 20, 50)
- MACD
- Bollinger Bands
- Rolling Volatility
- Daily Returns
- Lag Features
- Trading Volume Features

---

## 📂 Prediction History

Every prediction is automatically recorded with:

- Prediction Date
- Target Trading Date
- Stock Symbol
- Current Closing Price
- Predicted Closing Price
- Actual Closing Price (after verification)
- Prediction Status

---

## ✅ Automatic Prediction Verification

Unlike most ML stock prediction projects, StockVision automatically verifies predictions after the target trading day.

The application:

- Downloads the actual closing price
- Updates prediction history automatically
- Calculates prediction completion
- Marks predictions as **Verified**

---

## 🎨 Interactive Dashboard

The application includes multiple pages:

- 🏠 Home
- 📈 Dashboard
- 📚 Prediction History
- 📊 Live Market Data
- ℹ️ About

Features include:

- Company Search
- Live Predictions
- Interactive Metrics
- Theme Switching (System / Dark / Light)
- Modern Glassmorphism UI
- Responsive Layout

---
# 🏗️ System Architecture

```text
                    +----------------------+
                    |    Streamlit UI      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Prediction Engine    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Live Yahoo Finance   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Feature Engineering  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Linear Regression    |
                    | Prediction Model     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Prediction History   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Auto Verification    |
                    +----------------------+
```

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python |
| **Machine Learning** | Scikit-Learn (Linear Regression) |
| **Data Processing** | Pandas, NumPy |
| **Technical Indicators** | TA Library |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Live Market Data** | Yahoo Finance (`yfinance`) |
| **Frontend** | Streamlit |
| **Model Storage** | Joblib |
| **Model Training** | Scikit-Learn |
| **Deployment** | Streamlit Community Cloud |

---

# 📂 Project Structure

```text
StockVision-Forecast/
│
├── dataset/
│   ├── raw/
│   ├── processed/
│   └── live/
│
├── models/
│   ├── best_model.pkl
│   ├── feature_columns.pkl
│   ├── ticker_encoder.pkl
│   └── metrics.json
│
├── reports/
│   ├── prediction_history.csv
│   └── EDA Charts
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── training.py
│   ├── predictor.py
│   ├── live_data.py
│   ├── history.py
│   ├── accuracy.py
│   └── startup.py
│
├── streamlit_app/
│   ├── app.py
│   ├── pages/
│   └── assets/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---
# 🤖 Machine Learning Pipeline

StockVision Forecast V2 follows a complete end-to-end Machine Learning workflow.

```text
Raw Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Train / Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization
      │
      ▼
Live Prediction
      │
      ▼
Prediction History
      │
      ▼
Automatic Verification
```

---

## 📥 Data Collection

- Historical S&P 500 stock dataset
- Live market data from Yahoo Finance
- 472 supported companies
- OHLCV (Open, High, Low, Close, Volume) data

---

## 🧹 Data Preprocessing

The preprocessing pipeline performs:

- Missing value handling
- Date formatting
- Duplicate removal
- Data validation
- Feature consistency checks

---

## ⚙️ Feature Engineering

The model generates multiple technical indicators before prediction.

### Price-Based Features

- Daily Returns
- Lag Features
- Rolling Volatility

### Trend Indicators

- Moving Average (5)
- Moving Average (10)
- Moving Average (20)
- Moving Average (50)
- Exponential Moving Average (EMA)

### Momentum Indicators

- Relative Strength Index (RSI)
- MACD

### Volatility Indicators

- Bollinger Bands

---

## 🧠 Model Training

The final production model uses:

- **Linear Regression**

Training follows industry best practices:

- Chronological Train-Test Split
- No Data Leakage
- Feature Alignment
- Saved Model Artifacts using Joblib

---

## 📈 Live Prediction Workflow

Whenever a prediction is requested, the application:

1. Downloads the latest market data
2. Calculates all required technical indicators
3. Aligns features with the trained model
4. Predicts the next trading day's closing price
5. Saves prediction history
6. Stores live market data locally

---

## ✅ Automatic Prediction Verification

After the target trading day has completed, the application automatically:

- Downloads the actual closing price
- Updates prediction history
- Changes prediction status from **Pending** to **Verified**
- Stores the verified closing price

This creates a continuous prediction tracking system similar to production forecasting applications.

---
# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/StockVision-Forecast.git

cd StockVision-Forecast
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Launch the Streamlit application:

```bash
streamlit run streamlit_app/app.py
```

The application will automatically:

- Initialize the project
- Verify pending predictions
- Load the trained model
- Load cached live market data
- Open the dashboard in your browser

---

# 🌐 Deployment

StockVision Forecast V2 is designed for deployment on **Streamlit Community Cloud**.

Deployment requires:

- Python 3.11+
- `requirements.txt`
- Trained model files inside the `models/` directory
- Processed dataset
- Prediction history file

No additional backend server is required.

---

# 📊 Application Workflow

```text
User Selects Company
          │
          ▼
Download Latest Market Data
          │
          ▼
Feature Engineering
          │
          ▼
Load Trained Model
          │
          ▼
Predict Next Trading Day Close
          │
          ▼
Store Prediction History
          │
          ▼
Automatic Verification
```

---

# 📸 Application Screenshots

> Screenshots will be added after deployment.

Recommended screenshots:

- Dashboard
- Home Page
- Prediction Result
- Prediction History
- Live Market Data
- About Page

---
# 🚀 Future Enhancements

The following features are planned for future versions of StockVision:

- 🔮 Multi-day Stock Forecasting (3-Day / 5-Day / 7-Day)
- 🤖 Deep Learning Models (LSTM, GRU, Transformer)
- 📈 Candlestick Charts with Technical Indicators
- 📰 Financial News Sentiment Analysis
- 📧 Email Notifications for Predictions
- ☁️ Cloud Database Integration
- 👤 User Authentication & Personalized Watchlists
- 📱 Mobile Responsive Dashboard
- 📊 Model Performance Comparison Dashboard
- 🌍 Support for Global Stock Markets

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use
- ✅ Modify
- ✅ Distribute
- ✅ Fork

for both personal and commercial purposes while retaining the original license notice.

---

# 🙏 Acknowledgements

Special thanks to the following open-source projects and communities:

- Yahoo Finance (`yfinance`)
- Streamlit
- Scikit-Learn
- Plotly
- Pandas
- NumPy
- TA Library

Their tools and libraries made this project possible.

---

# 👨‍💻 Author

**THUGADAM SHANMUKASAI**

B.Tech – Computer Science & Engineering (AI & ML)

Machine Learning | Data Science | Python | Streamlit

---

⭐ If you found this project useful, consider giving the repository a **Star** on GitHub!

---
