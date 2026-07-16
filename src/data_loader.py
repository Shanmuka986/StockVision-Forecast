"""
data_loader.py

Loads the raw stock dataset and performs basic validation.
"""

from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_DIR
from src.utils import file_exists, print_section


DATA_FILE_NAME = "sp500_stocks.csv"


def load_dataset() -> pd.DataFrame:
    """
    Load the raw stock dataset.

    Returns
    -------
    pd.DataFrame
        Loaded stock dataset.
    """
    dataset_path = RAW_DATA_DIR / DATA_FILE_NAME

    if not file_exists(dataset_path):
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    print_section("Loading Dataset")

    dataframe = pd.read_csv(dataset_path)

    print(f"Dataset loaded successfully.")
    print(f"Shape: {dataframe.shape}")

    return dataframe


def display_dataset_info(dataframe: pd.DataFrame) -> None:
    """
    Display dataset information.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Loaded dataset.
    """

    print_section("Dataset Information")

    print("\nFirst Five Rows:\n")
    print(dataframe.head())

    print("\nColumn Names:\n")
    print(list(dataframe.columns))

    print("\nData Types:\n")
    print(dataframe.dtypes)

    print("\nMissing Values:\n")
    print(dataframe.isnull().sum())
if __name__ == "__main__":
    df = load_dataset()
    display_dataset_info(df)