"""
feature_engineering.py

Feature Engineering for StockVision Forecast V2.
"""

import pandas as pd

from ta.momentum import RSIIndicator

from ta.trend import (
    EMAIndicator,
    MACD,
)

from ta.volatility import BollingerBands

from src.config import PROCESSED_DATA_DIR
from src.utils import print_section
from sklearn.preprocessing import LabelEncoder

# ==========================================================
# Load Dataset
# ==========================================================

def load_cleaned_dataset() -> pd.DataFrame:

    dataset_path = (
        PROCESSED_DATA_DIR /
        "cleaned_stock_data.csv"
    )

    dataframe = pd.read_csv(
        dataset_path,
        parse_dates=["Date"]
    )

    dataframe = dataframe.sort_values(
        by=["Ticker", "Date"]
    ).reset_index(drop=True)

    return dataframe


# ==========================================================
# Target
# ==========================================================

def create_target(dataframe):

    print_section("Creating Target Variable")

    dataframe["Next_Close"] = (
        dataframe
        .groupby("Ticker")["Close"]
        .shift(-1)
    )

    print("Target column created.")

    return dataframe


# ==========================================================
# Lag Features
# ==========================================================

def create_lag_features(dataframe):

    print_section("Creating Lag Features")

    grouped = dataframe.groupby("Ticker")

    dataframe["Lag_1_Close"] = grouped["Close"].shift(1)
    dataframe["Lag_2_Close"] = grouped["Close"].shift(2)
    dataframe["Lag_3_Close"] = grouped["Close"].shift(3)

    dataframe["Lag_1_Open"] = grouped["Open"].shift(1)
    dataframe["Lag_1_High"] = grouped["High"].shift(1)
    dataframe["Lag_1_Low"] = grouped["Low"].shift(1)

    dataframe["Lag_1_Volume"] = grouped["Volume"].shift(1)

    print("Lag features created.")

    return dataframe


# ==========================================================
# Daily Return
# ==========================================================

def create_daily_return(dataframe):

    print_section("Creating Daily Return")

    dataframe["Daily_Return"] = (
        dataframe
        .groupby("Ticker")["Close"]
        .pct_change()
    )

    print("Daily Return created.")

    return dataframe


# ==========================================================
# Moving Averages
# ==========================================================

def create_moving_averages(dataframe):

    print_section("Creating Moving Averages")

    grouped = dataframe.groupby("Ticker")["Close"]

    dataframe["MA_5"] = (
        grouped.transform(
            lambda x: x.rolling(5).mean()
        )
    )

    dataframe["MA_10"] = (
        grouped.transform(
            lambda x: x.rolling(10).mean()
        )
    )

    dataframe["MA_20"] = (
        grouped.transform(
            lambda x: x.rolling(20).mean()
        )
    )

    dataframe["MA_50"] = (
        grouped.transform(
            lambda x: x.rolling(50).mean()
        )
    )

    print("Moving averages created.")

    return dataframe
# ==========================================================
# Add this function BELOW create_moving_averages()
# ==========================================================

def create_rolling_volatility(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Create 20-day rolling volatility using
    Daily_Return.
    """

    print_section("Creating Rolling Volatility")

    dataframe["Rolling_Volatility"] = (
        dataframe
        .groupby("Ticker")["Daily_Return"]
        .transform(
            lambda x: x.rolling(
                window=20
            ).std()
        )
    )

    print("Rolling Volatility created.")

    return dataframe
# ==========================================================
# Technical Indicators
# ==========================================================

def create_technical_indicators(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Create RSI, EMA, MACD and
    Bollinger Bands.
    """

    print_section(
        "Creating Technical Indicators"
    )

    result = []

    for _, company_df in dataframe.groupby("Ticker"):

        company_df = company_df.copy()

        # -----------------------------
        # RSI
        # -----------------------------

        company_df["RSI_14"] = RSIIndicator(
            close=company_df["Close"],
            window=14,
        ).rsi()

        # -----------------------------
        # EMA
        # -----------------------------

        company_df["EMA_20"] = EMAIndicator(
            close=company_df["Close"],
            window=20,
        ).ema_indicator()

        # -----------------------------
        # MACD
        # -----------------------------

        macd = MACD(
            close=company_df["Close"]
        )

        company_df["MACD"] = (
            macd.macd()
        )

        company_df["MACD_Signal"] = (
            macd.macd_signal()
        )

        company_df["MACD_Hist"] = (
            macd.macd_diff()
        )

        # -----------------------------
        # Bollinger Bands
        # -----------------------------

        bb = BollingerBands(
            close=company_df["Close"],
            window=20,
            window_dev=2,
        )

        company_df["BB_Upper"] = (
            bb.bollinger_hband()
        )

        company_df["BB_Middle"] = (
            bb.bollinger_mavg()
        )

        company_df["BB_Lower"] = (
            bb.bollinger_lband()
        )

        result.append(company_df)

    dataframe = (
        pd.concat(result)
        .sort_values(
            ["Ticker", "Date"]
        )
        .reset_index(drop=True)
    )

    print(
        "Technical indicators created."
    )

    return dataframe
# ==========================================================
# Ticker Encoding
# ==========================================================

def create_ticker_encoding(
    dataframe: pd.DataFrame
) -> tuple[pd.DataFrame, LabelEncoder]:
    """
    Encode ticker symbols into numerical values.
    """

    print_section("Creating Ticker Encoding")

    encoder = LabelEncoder()

    dataframe["Ticker_Encoded"] = encoder.fit_transform(
        dataframe["Ticker"]
    )

    print("Ticker encoding created.")
    print(f"Total Unique Tickers: {len(encoder.classes_)}")

    return dataframe, encoder
# ==========================================================
# Missing Value Analysis
# ==========================================================

def analyze_missing_values(
    dataframe: pd.DataFrame
) -> None:
    """
    Analyze missing values created during
    feature engineering.
    """

    print_section("Missing Value Analysis")

    missing = dataframe.isna().sum()

    missing = missing[missing > 0].sort_values(ascending=False)

    print(missing)

    print("\nTotal Rows:", len(dataframe))
# ==========================================================
# Remove Invalid Rows
# ==========================================================

def remove_invalid_rows(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Remove rows with missing values created during
    feature engineering and report statistics.
    """

    print_section("Removing Invalid Rows")

    rows_before = len(dataframe)

    dataframe = (
        dataframe
        .dropna()
        .reset_index(drop=True)
    )

    rows_after = len(dataframe)

    rows_removed = rows_before - rows_after

    retained_percentage = (
        rows_after / rows_before
    ) * 100

    print(f"Rows Before     : {rows_before:,}")
    print(f"Rows After      : {rows_after:,}")
    print(f"Rows Removed    : {rows_removed:,}")
    print(f"Data Retained   : {retained_percentage:.2f}%")

    return dataframe
# ==========================================================
# Save Featured Dataset
# ==========================================================

def save_featured_dataset(
    dataframe: pd.DataFrame
) -> None:
    """
    Save the engineered dataset.
    """

    print_section("Saving Featured Dataset")

    output_path = (
        PROCESSED_DATA_DIR /
        "featured_stock_data.csv"
    )

    dataframe.to_csv(
        output_path,
        index=False
    )

    print("Dataset saved successfully.")
    print(f"Location: {output_path}")
# ==========================================================
# Prepare Live Features
# ==========================================================

import joblib

from src.config import MODELS_DIR


def prepare_live_features(
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Prepare live stock data for prediction.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Live stock data downloaded from Yahoo Finance.

    Returns
    -------
    pd.DataFrame
        Latest feature vector ready for prediction.
    """

    print_section("Preparing Live Features")

    # ------------------------------------------------------
    # Lag Features
    # ------------------------------------------------------

    dataframe = create_lag_features(dataframe)

    # ------------------------------------------------------
    # Daily Return
    # ------------------------------------------------------

    dataframe = create_daily_return(dataframe)

    # ------------------------------------------------------
    # Moving Averages
    # ------------------------------------------------------

    dataframe = create_moving_averages(dataframe)

    # ------------------------------------------------------
    # Rolling Volatility
    # ------------------------------------------------------

    dataframe = create_rolling_volatility(dataframe)

    # ------------------------------------------------------
    # Technical Indicators
    # ------------------------------------------------------

    dataframe = create_technical_indicators(dataframe)

    # ------------------------------------------------------
    # Remove rows that still contain NaN
    # ------------------------------------------------------

    dataframe = dataframe.dropna().reset_index(drop=True)

    if dataframe.empty:
        raise ValueError(
            "Not enough historical data to create features."
        )

    # ------------------------------------------------------
    # Encode Company
    # ------------------------------------------------------

    encoder = joblib.load(
        MODELS_DIR / "ticker_encoder.pkl"
    )

    dataframe["Ticker_Encoded"] = encoder.transform(
        dataframe["Ticker"]
    )

    # ------------------------------------------------------
    # Load Feature Order
    # ------------------------------------------------------

    feature_columns = joblib.load(
        MODELS_DIR / "feature_columns.pkl"
    )

    latest_row = dataframe.iloc[[-1]]

    latest_row = latest_row[feature_columns]

    print("Live features prepared successfully.")

    return latest_row

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    df = load_cleaned_dataset()

    df = create_target(df)

    df = create_lag_features(df)

    df = create_daily_return(df)

    df = create_moving_averages(df)

    df = create_rolling_volatility(df)

    df = create_technical_indicators(df)

    df, encoder = create_ticker_encoding(df)

    analyze_missing_values(df)

    df = remove_invalid_rows(df)

    save_featured_dataset(df)

    print()

    print(df.head(15))

    print()

    print(df.info())
   