"""
eda.py

Exploratory Data Analysis (EDA) for the
StockVision Forecast V2 project.

Phase 3
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.config import PROCESSED_DATA_DIR, REPORTS_DIR
from src.utils import create_directory, print_section


# ==========================================================
# Load Dataset
# ==========================================================

def load_cleaned_dataset() -> pd.DataFrame:
    """
    Load the cleaned dataset.
    """

    dataset_path = (
        PROCESSED_DATA_DIR /
        "cleaned_stock_data.csv"
    )

    dataframe = pd.read_csv(
        dataset_path,
        parse_dates=["Date"]
    )

    return dataframe


# ==========================================================
# Dataset Overview
# ==========================================================

def dataset_overview(dataframe: pd.DataFrame) -> None:
    """
    Display general dataset information.
    """

    print_section("Dataset Overview")

    print(f"Shape : {dataframe.shape}")

    memory = dataframe.memory_usage(
        deep=True
    ).sum() / (1024 ** 2)

    print(f"Memory Usage : {memory:.2f} MB")

    print("\nColumns\n")
    print(list(dataframe.columns))

    print("\nData Types\n")
    print(dataframe.dtypes)


# ==========================================================
# Descriptive Statistics
# ==========================================================

def descriptive_statistics(dataframe: pd.DataFrame) -> None:
    """
    Display descriptive statistics.
    """

    print_section("Descriptive Statistics")

    print(dataframe.describe())


# ==========================================================
# Company Analysis
# ==========================================================

def company_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze company-wise record distribution.
    """

    print_section("Company Analysis")

    company_counts = (
        dataframe["Ticker"]
        .value_counts()
        .sort_index()
    )

    print(f"Total Companies : {company_counts.shape[0]}")
    print(f"Average Records per Company : {company_counts.mean():.2f}")
    print(f"Minimum Records : {company_counts.min()}")
    print(f"Maximum Records : {company_counts.max()}")

    print("\nTop 10 Companies by Record Count\n")
    print(company_counts.sort_values(ascending=False).head(10))

    print("\nBottom 10 Companies by Record Count\n")
    print(company_counts.sort_values().head(10))


# ==========================================================
# Time Analysis
# ==========================================================

def time_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze time coverage.
    """

    print_section("Time Analysis")

    start_date = dataframe["Date"].min()
    end_date = dataframe["Date"].max()

    print(f"Start Date : {start_date.date()}")
    print(f"End Date   : {end_date.date()}")

    total_days = (end_date - start_date).days

    print(f"Total Calendar Days : {total_days}")

    total_years = dataframe["Date"].dt.year.nunique()

    print(f"Trading Years : {total_years}")

    records_per_year = (
        dataframe.groupby(
            dataframe["Date"].dt.year
        )
        .size()
    )

    print("\nRecords Per Year\n")
    print(records_per_year)


# ==========================================================
# Price Analysis
# ==========================================================

def price_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze price columns.
    """

    print_section("Price Analysis")

    price_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
    ]

    statistics = pd.DataFrame(
        index=price_columns,
        columns=[
            "Minimum",
            "Maximum",
            "Mean",
            "Median",
            "Std Dev",
        ]
    )

    for column in price_columns:

        statistics.loc[column, "Minimum"] = dataframe[column].min()
        statistics.loc[column, "Maximum"] = dataframe[column].max()
        statistics.loc[column, "Mean"] = round(dataframe[column].mean(), 2)
        statistics.loc[column, "Median"] = round(dataframe[column].median(), 2)
        statistics.loc[column, "Std Dev"] = round(dataframe[column].std(), 2)

    print(statistics)


# ==========================================================
# Volume Analysis
# ==========================================================

def volume_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze trading volume.
    """

    print_section("Volume Analysis")

    volume = dataframe["Volume"]

    print(f"Minimum Volume          : {volume.min():,.0f}")
    print(f"Maximum Volume          : {volume.max():,.0f}")
    print(f"Mean Volume             : {volume.mean():,.2f}")
    print(f"Median Volume           : {volume.median():,.2f}")
    print(f"Standard Deviation      : {volume.std():,.2f}")

    zero_volume = (volume == 0).sum()

    print(f"Zero Volume Records     : {zero_volume:,}")


# ==========================================================
# Correlation Analysis
# ==========================================================

def correlation_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze numerical correlations.
    """

    print_section("Correlation Analysis")

    correlation_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
    ]

    correlation_matrix = dataframe[
        correlation_columns
    ].corr()

    print(correlation_matrix)


# ==========================================================
# Visualizations
# ==========================================================

def generate_visualizations(dataframe: pd.DataFrame) -> None:
    """
    Generate and save EDA visualizations.
    """

    print_section("Generating Visualizations")

    create_directory(REPORTS_DIR)

    # Sample only for plotting
    sample_size = min(100000, len(dataframe))

    sample_df = dataframe.sample(
        n=sample_size,
        random_state=42
    )

    # ------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.hist(
        sample_df["Close"],
        bins=50
    )

    plt.title("Closing Price Distribution")
    plt.xlabel("Closing Price")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        REPORTS_DIR / "close_distribution.png",
        dpi=300
    )

    plt.close()

    # ------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.hist(
        sample_df["Volume"],
        bins=50
    )

    plt.title("Volume Distribution")
    plt.xlabel("Volume")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        REPORTS_DIR / "volume_distribution.png",
        dpi=300
    )

    plt.close()

    # ------------------------------------------------------

    correlation_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
    ]

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        dataframe[correlation_columns].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        REPORTS_DIR / "correlation_heatmap.png",
        dpi=300
    )

    plt.close()

    # ------------------------------------------------------

    top_companies = (
        dataframe["Ticker"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    top_companies.plot(
        kind="bar"
    )

    plt.title("Top 10 Companies by Record Count")
    plt.xlabel("Ticker")
    plt.ylabel("Records")

    plt.tight_layout()

    plt.savefig(
        REPORTS_DIR / "top_10_companies.png",
        dpi=300
    )

    plt.close()

    # ------------------------------------------------------

    records_per_year = (
        dataframe.groupby(
            dataframe["Date"].dt.year
        )
        .size()
    )

    plt.figure(figsize=(12, 6))

    records_per_year.plot()

    plt.title("Records Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Records")

    plt.tight_layout()

    plt.savefig(
        REPORTS_DIR / "records_per_year.png",
        dpi=300
    )

    plt.close()

    print("All visualizations saved successfully.")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    df = load_cleaned_dataset()

    dataset_overview(df)

    descriptive_statistics(df)

    company_analysis(df)

    time_analysis(df)

    price_analysis(df)

    volume_analysis(df)

    correlation_analysis(df)

    generate_visualizations(df)

    print_section("EDA Completed Successfully")