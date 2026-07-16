"""
split.py

Chronological Train/Test Split
for StockVision Forecast V2.
"""

import pandas as pd

from src.config import PROCESSED_DATA_DIR
from src.utils import print_section


# ==========================================================
# Load Featured Dataset
# ==========================================================

def load_featured_dataset() -> pd.DataFrame:
    """
    Load engineered dataset.
    """

    dataset_path = (
        PROCESSED_DATA_DIR /
        "featured_stock_data.csv"
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
# Per-Ticker Chronological Split
# ==========================================================

def chronological_split(
    dataframe: pd.DataFrame,
    train_ratio: float = 0.80
):
    """
    Perform chronological split
    independently for each ticker.
    """

    print_section(
        "Chronological Train/Test Split"
    )

    train_list = []

    test_list = []

    total_companies = dataframe["Ticker"].nunique()

    print(f"Companies : {total_companies}")

    for _, company_df in dataframe.groupby("Ticker"):

        split_index = int(
            len(company_df) * train_ratio
        )

        train_list.append(
            company_df.iloc[:split_index]
        )

        test_list.append(
            company_df.iloc[split_index:]
        )

    train_df = (
        pd.concat(train_list)
        .reset_index(drop=True)
    )

    test_df = (
        pd.concat(test_list)
        .reset_index(drop=True)
    )

    print()

    print(f"Training Rows : {len(train_df):,}")
    print(f"Testing Rows  : {len(test_df):,}")

    return train_df, test_df


# ==========================================================
# Create X and y
# ==========================================================

def create_features_target(
    dataframe: pd.DataFrame
):

    X = dataframe.drop(
        columns=[
            "Ticker",
            "Date",
            "Next_Close",
        ]
    )

    y = dataframe["Next_Close"]

    return X, y
# ==========================================================
# Save Split Datasets
# ==========================================================

def save_split_datasets(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> None:
    """
    Save train/test datasets for model training.
    """

    print_section("Saving Split Datasets")

    output_dir = PROCESSED_DATA_DIR

    train_df.to_csv(
        output_dir / "train.csv",
        index=False
    )

    test_df.to_csv(
        output_dir / "test.csv",
        index=False
    )

    X_train.to_csv(
        output_dir / "X_train.csv",
        index=False
    )

    X_test.to_csv(
        output_dir / "X_test.csv",
        index=False
    )

    y_train.to_frame(name="Next_Close").to_csv(
        output_dir / "y_train.csv",
        index=False
    )

    y_test.to_frame(name="Next_Close").to_csv(
        output_dir / "y_test.csv",
        index=False
    )

    print("All datasets saved successfully.")

    print(f"Location : {output_dir}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    df = load_featured_dataset()

    train_df, test_df = chronological_split(df)

    X_train, y_train = create_features_target(train_df)

    X_test, y_test = create_features_target(test_df)

    print_section("Dataset Shapes")

    print(f"X_train : {X_train.shape}")
    print(f"y_train : {y_train.shape}")

    print()

    print(f"X_test  : {X_test.shape}")
    print(f"y_test  : {y_test.shape}")

    print()

    print("Train Date Range")
    print(train_df["Date"].min())
    print(train_df["Date"].max())

    print()

    print("Test Date Range")
    print(test_df["Date"].min())
    print(test_df["Date"].max())

    save_split_datasets(
        train_df,
        test_df,
        X_train,
        X_test,
        y_train,
        y_test,
    )