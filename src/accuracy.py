"""
accuracy.py

Automatically verifies pending predictions
using Yahoo Finance closing prices.
"""

import pandas as pd
import yfinance as yf

from src.database.prediction_db import (
    get_pending_predictions,
    update_prediction,
)

# ==========================================================
# History File
# ==========================================================

DOWNLOAD_BUFFER_DAYS = 3

STATUS_PENDING = "Pending"

STATUS_VERIFIED = "Verified"

# ==========================================================
# Verification Settings
# ==========================================================

DOWNLOAD_BUFFER_DAYS = 3

STATUS_PENDING = "Pending"

STATUS_VERIFIED = "Verified"


# ==========================================================
# Update Prediction Accuracy
# ==========================================================

def update_prediction_accuracy():
    """
    Update all pending predictions whose target
    trading day has already completed.

    Returns
    -------
    int
        Number of predictions verified.
    """

    # ------------------------------------------------------
    # Check History File
    # ------------------------------------------------------
    history = get_pending_predictions()
    if not history:
        print("No pending predictions found.")
        return 0
 

    # ------------------------------------------------------
    # Current Date
    # ------------------------------------------------------

    today = pd.Timestamp.today().normalize()

    updated = 0

    print("=" * 60)
    print("Prediction Verification Started")
    print("=" * 60)
    print(f"Today's Date : {today.date()}")
    print(f"Total Records : {len(history)}")
    print()

      # ------------------------------------------------------
    # Check Every Prediction
    # ------------------------------------------------------

    for  row in history:

        # Skip already verified predictions
        if row["prediction_status"] != STATUS_PENDING:

            continue

        ticker = str(row["ticker"]).upper()

        target_date = pd.to_datetime(
            row["target_trading_date"]
        ).normalize()

        print("-" * 60)
        print(f"Ticker       : {ticker}")
        print(f"Target Date  : {target_date.date()}")
        print(f"Today        : {today.date()}")

        # --------------------------------------------------
        # Wait until the target trading day has finished
        # --------------------------------------------------

        if today <= target_date:

            print("Status       : Waiting for market close")
            print()

            continue

        print("Status       : Ready for verification")
        print()

        try:

            # --------------------------------------------------
            # Download data around target trading day
            # --------------------------------------------------

            start_date = target_date - pd.Timedelta(
                days=DOWNLOAD_BUFFER_DAYS
            )

            end_date = target_date + pd.Timedelta(
                days=DOWNLOAD_BUFFER_DAYS
            )

            print(
                f"Downloading market data for {ticker}..."
            )

            latest = yf.download(

                ticker,

                start=start_date.strftime("%Y-%m-%d"),

                end=end_date.strftime("%Y-%m-%d"),

                progress=False,

                auto_adjust=False

            )

            if latest.empty:

                print("No market data found.")
                print()

                continue

            latest = latest.reset_index()

            # --------------------------------------------------
            # Normalize Date Column
            # --------------------------------------------------

            date_column = latest.columns[0]

            latest[date_column] = pd.to_datetime(
                latest[date_column]
            ).dt.normalize()

            # --------------------------------------------------
            # Find first available trading day
            # on or after target date
            # --------------------------------------------------

            target_rows = latest[
                latest[date_column] >= target_date
            ]

            if target_rows.empty:

                print(
                    "No trading session available."
                )
                print()

                continue

            verification_row = target_rows.iloc[0]
          

            close_value = verification_row["Close"]
            if isinstance(close_value, pd.Series):
                    close_value = close_value.iloc[0]
            actual_close = round(
                float(close_value),
                2



            )
    

            actual_date = verification_row[
                date_column
            ].date()

            print(
                f"Verified Date : {actual_date}"
            )

            print(
                f"Actual Close  : ${actual_close}"
            )

            print()

                        # --------------------------------------------------
            # Update Prediction History
            # --------------------------------------------------

            update_prediction(
                prediction_id=row["prediction_id"],
                actual_close=actual_close,
            )

            updated += 1

            print(
                f"SUCCESS: {ticker} verified successfully."
            )

            print()

        except Exception as error:

            print("=" * 60)
            print(f"Verification failed for {ticker}")
            print(f"Reason: {error}")
            print("=" * 60)
            print()

            continue

    # ------------------------------------------------------
    # Save Updated History
    # ------------------------------------------------------

 

    print("=" * 60)
    print("Prediction Verification Completed")
    print("=" * 60)
    print(f"Rows Updated : {updated}")
    print()

    return updated

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    updated = update_prediction_accuracy()

    print()

    print("=" * 60)

    print("Prediction Verification")

    print("=" * 60)

    print()

    print(f"Rows Updated : {updated}")