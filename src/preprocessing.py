"""
preprocessing.py

Validates and preprocesses the raw stock dataset.
"""

import pandas as pd

from src.config import PROCESSED_DATA_DIR
from src.data_loader import load_dataset
from src.utils import create_directory, print_section


REQUIRED_COLUMNS = [
    "Ticker",
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Adj Close",
    "Volume",
]


def validate_dataset(dataframe: pd.DataFrame) -> None:
    """
    Validate the raw stock dataset.
    """

    print_section("Dataset Validation")

    if dataframe.empty:
        raise ValueError("Dataset is empty.")

    print("Dataset is not empty.")
    print(f"Dataset Shape : {dataframe.shape}")

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("Required columns verified.")

    print("\nMissing Values")
    print(dataframe.isnull().sum())

    duplicate_count = dataframe.duplicated().sum()
    print(f"\nDuplicate Rows : {duplicate_count}")

    print("\nData Types")
    print(dataframe.dtypes)

    print(
        f"\nUnique Companies : "
        f"{dataframe['Ticker'].nunique()}"
    )

    dates = pd.to_datetime(dataframe["Date"])

    print("\nDate Range")
    print(f"Start : {dates.min().date()}")
    print(f"End   : {dates.max().date()}")

    price_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
    ]

    for column in price_columns:
        negative_values = (dataframe[column] < 0).sum()
        print(f"Negative values in {column}: {negative_values}")

    negative_volume = (dataframe["Volume"] < 0).sum()

    print(f"Negative Volume Values : {negative_volume}")

    print("\nDataset validation completed successfully.")


def clean_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the validated dataset.
    """

    print_section("Data Cleaning")

    dataframe = dataframe.copy()

    # Convert Date column
    dataframe["Date"] = pd.to_datetime(dataframe["Date"])

    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()

    # Sort by Ticker and Date
    dataframe = dataframe.sort_values(
        by=["Ticker", "Date"]
    )

    # Reset index
    dataframe = dataframe.reset_index(drop=True)

    print("Date converted to datetime.")
    print("Dataset sorted by Ticker and Date.")
    print("Index reset.")

    return dataframe


def save_processed_dataset(dataframe: pd.DataFrame) -> None:
    """
    Save cleaned dataset.
    """

    print_section("Saving Processed Dataset")

    create_directory(PROCESSED_DATA_DIR)

    output_path = (
        PROCESSED_DATA_DIR /
        "cleaned_stock_data.csv"
    )

    dataframe.to_csv(output_path, index=False)

    print(f"Dataset saved successfully.")
    print(f"Location : {output_path}")


if __name__ == "__main__":

    df = load_dataset()

    validate_dataset(df)

    cleaned_df = clean_dataset(df)

    save_processed_dataset(cleaned_df)

    print_section("Preprocessing Completed")
    print(cleaned_df.head())