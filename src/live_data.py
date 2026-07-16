"""
live_data.py

Download latest stock market data
from Yahoo Finance.
"""

from datetime import datetime

import pandas as pd
from streamlit import dataframe
import yfinance as yf

from src.config import LIVE_DATA_DIR
from src.utils import print_section


# ==========================================================
# Download Latest Stock Data
# ==========================================================

def download_stock_data(
    ticker: str,
    period: str = "6mo",
    interval: str = "1d",
) -> pd.DataFrame:
    """
    Download latest stock market data
    from Yahoo Finance.
    """

    print_section("Downloading Latest Stock Data")

    dataframe = yf.download(
        tickers=ticker.upper(),
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )

    if dataframe.empty:
        raise ValueError(
            f"No data found for ticker : {ticker}"
        )

    dataframe = dataframe.reset_index()

    # ======================================================
    # Handle MultiIndex Columns
    # ======================================================

    if isinstance(
        dataframe.columns,
        pd.MultiIndex
    ):
        dataframe.columns = (
            dataframe.columns.get_level_values(0)
        )

    # ======================================================
    # Keep Required Columns
    # ======================================================

    required_columns = [

        "Date",

        "Open",

        "High",

        "Low",

        "Close",

        "Adj Close",

        "Volume"

    ]

    dataframe = dataframe[
        required_columns
    ]

    dataframe["Ticker"] = ticker.upper()

    dataframe = dataframe.sort_values(
        by="Date"
    ).reset_index(drop=True)

    # ======================================================
    # Save Live Dataset
    # ======================================================

    # Keep only one dataset per company.
    # Each new download replaces the previous file.

    file_name = f"{ticker.upper()}.csv"

    dataframe.to_csv(
        LIVE_DATA_DIR / file_name,
        index=False
        )
    print()
    print(f"Live Data Updated : {file_name}")
    # ======================================================
    # Display Information
    # ======================================================

    print()

    print(f"Ticker          : {ticker.upper()}")

    print(
        f"Rows Downloaded : {len(dataframe)}"
    )

    print()

    print("Columns")

    print(
        dataframe.columns.tolist()
    )

    print()

    print(dataframe.head())

    return dataframe


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    df = download_stock_data(
        ticker="AAPL"
    )