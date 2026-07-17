"""
history.py

Store prediction history in PostgreSQL
for StockVision Forecast V2.
"""

from datetime import datetime
from uuid import uuid4

import pandas as pd
from pandas.tseries.offsets import BusinessDay
from src.company_mapping import COMPANY_MAPPING


from src.database.prediction_db import save_prediction as db_save_prediction


# ==========================================================
# Save Prediction
# ==========================================================

def save_prediction(result: dict):
    """
    Save prediction history into PostgreSQL.
    """

    # ------------------------------------------------------
    # Current Time
    # ------------------------------------------------------

    now = datetime.now()

    prediction_date = now.date()

    target_date = (
        pd.Timestamp(now) + BusinessDay(1)
    ).date()

    # ------------------------------------------------------
    # Prediction ID
    # ------------------------------------------------------

    prediction_id = str(uuid4())[:8]

    # ------------------------------------------------------
    # Save to Database
    # ------------------------------------------------------

    db_save_prediction(
        prediction_id=prediction_id,
        prediction_date=prediction_date,
        target_trading_date=target_date,
        ticker=result["Ticker"],
        company_name=COMPANY_MAPPING.get(
            result["Ticker"],
            result["Ticker"]
        ),
        today_close=result["Today's Close"],
        predicted_close=result["Predicted Close"],
    )

    print()
    print("Prediction saved successfully.")
    print(f"Prediction ID : {prediction_id}")


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample = {

        "Ticker": "AAPL",

        "Company Name": "Apple Inc.",

        "Today's Close": 315.32,

        "Predicted Close": 314.87,

        "Change": -0.45,

        "Change %": -0.14,

        "Direction": "DOWN"

    }

    save_prediction(sample)