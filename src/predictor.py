"""
predictor.py

Live prediction pipeline
for StockVision Forecast V2.
"""

import joblib

from src.config import MODELS_DIR
from src.live_data import download_stock_data
from src.feature_engineering import prepare_live_features
from src.history import save_prediction

# ==========================================================
# Load Model
# ==========================================================

def load_model():

    return joblib.load(
        MODELS_DIR / "best_model.pkl"
    )

# ==========================================================
# Predict Next Closing Price
# ==========================================================

def predict_stock(
    ticker: str
):
    """
    Predict next day's closing price and
    return complete prediction details.
    """

    # ------------------------------------------------------
    # Download Live Market Data
    # ------------------------------------------------------

    try:

        live_df = download_stock_data(
            ticker=ticker
        )

    except Exception as e:

        message = str(e)

        if (
            "RateLimit" in message
            or "Too Many Requests" in message
        ):

            raise RuntimeError(
                "Yahoo Finance is temporarily busy due to rate limiting. Please wait a minute and try again."
            )

        raise RuntimeError(message)

    # ------------------------------------------------------
    # Today's Close
    # ------------------------------------------------------

    today_close = float(
        live_df.iloc[-1]["Close"]
    )

    # ------------------------------------------------------
    # Prepare Features
    # ------------------------------------------------------

    X = prepare_live_features(
        live_df
    )

    # ------------------------------------------------------
    # Load Model
    # ------------------------------------------------------

    model = load_model()

    # ------------------------------------------------------
    # Prediction
    # ------------------------------------------------------

    predicted_close = float(
        model.predict(X)[0]
    )

    predicted_close = round(
        predicted_close,
        2
    )

    today_close = round(
        today_close,
        2
    )

    change = round(
        predicted_close - today_close,
        2
    )

    change_percent = round(
        (change / today_close) * 100,
        2
    )

    direction = (
        "UP"
        if change >= 0
        else "DOWN"
    )

    # ------------------------------------------------------
    # Prediction Result
    # ------------------------------------------------------

    result = {

        "Ticker": ticker,

        "Today's Close": today_close,

        "Predicted Close": predicted_close,

        "Change": change,

        "Change %": change_percent,

        "Direction": direction

    }

    # ------------------------------------------------------
    # Save Prediction History
    # ------------------------------------------------------

    save_prediction(result)

    return result

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    ticker = input(
        "Enter Stock Ticker : "
    ).upper()

    result = predict_stock(
        ticker
    )

    print()

    print("=" * 60)
    print("STOCK PREDICTION")
    print("=" * 60)

    for key, value in result.items():
        print(f"{key:<20}: {value}")