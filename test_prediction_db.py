"""
Test Database Operations
"""

from datetime import date, timedelta
from uuid import uuid4

from src.database.prediction_db import (
    save_prediction,
    get_prediction_history,
)

prediction_id = str(uuid4())[:8]

today = date.today()

target = today + timedelta(days=1)

save_prediction(
    prediction_id=prediction_id,
    prediction_date=today,
    target_trading_date=target,
    ticker="AAPL",
    company_name="Apple Inc.",
    today_close=210.55,
    predicted_close=212.13,
)

print("✅ Prediction inserted successfully.")

history = get_prediction_history()

print(f"\nTotal Records : {len(history)}\n")

print(history[0])