"""
history.py

Store prediction history for
StockVision Forecast V2.
"""

from datetime import datetime

import pandas as pd
from pandas.tseries.offsets import BusinessDay

from src.config import REPORTS_DIR

# ==========================================================
# History File
# ==========================================================

HISTORY_FILE = REPORTS_DIR / "prediction_history.csv"


# ==========================================================
# Save Prediction
# ==========================================================

def save_prediction(result: dict):
    """
    Save prediction history.
    """

    # ------------------------------------------------------
    # Current Time
    # ------------------------------------------------------

    now = datetime.now()

    target_date = (
        pd.Timestamp(now) + BusinessDay(1)
    ).strftime("%Y-%m-%d")

    # ------------------------------------------------------
    # Create Record
    # ------------------------------------------------------

    record = {

        "Prediction ID": None,

        "Prediction Date": now.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "Target Trading Date": target_date,

        "Ticker": result["Ticker"],

        "Today's Closing Price":
        result["Today's Close"],

        "Tomorrow's Predicted Closing Price":
        result["Predicted Close"],

        "Actual Closing Price": None,

        "Prediction Status": "Pending"

    }

    # ------------------------------------------------------
    # Load Existing History
    # ------------------------------------------------------

    if HISTORY_FILE.exists():

        history = pd.read_csv(
            HISTORY_FILE
        )

    else:

        history = pd.DataFrame()

    # ------------------------------------------------------
    # Prediction ID
    # ------------------------------------------------------

    if history.empty:

        record["Prediction ID"] = 1

    else:

        record["Prediction ID"] = (
            int(history["Prediction ID"].max())
            + 1
        )

    # ------------------------------------------------------
    # Append
    # ------------------------------------------------------

    history = pd.concat(

        [

            history,

            pd.DataFrame([record])

        ],

        ignore_index=True

    )

    # ------------------------------------------------------
    # Save
    # ------------------------------------------------------

    history.to_csv(

        HISTORY_FILE,

        index=False

    )

    print()

    print("Prediction saved successfully.")

    print(
        f"History File : {HISTORY_FILE.name}"
    )


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample = {

        "Ticker": "AAPL",

        "Today's Close": 315.32,

        "Predicted Close": 314.87,

        "Change": -0.45,

        "Change %": -0.14,

        "Direction": "DOWN"

    }

    save_prediction(sample)