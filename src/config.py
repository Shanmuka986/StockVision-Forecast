"""
config.py

Central configuration file for the
StockVision Forecast V2 project.
Contains project paths and
global configuration variables.
"""

from pathlib import Path

# ==========================================================
# Project Root Directory
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Dataset Directories
# ==========================================================

DATASET_DIR = BASE_DIR / "dataset"

RAW_DATA_DIR = DATASET_DIR / "raw"

PROCESSED_DATA_DIR = DATASET_DIR / "processed"

LIVE_DATA_DIR = DATASET_DIR / "live"

# ==========================================================
# Models Directory
# ==========================================================

MODELS_DIR = BASE_DIR / "models"

# ==========================================================
# Reports Directory
# ==========================================================

REPORTS_DIR = BASE_DIR / "reports"

# ==========================================================
# Notebooks Directory
# ==========================================================

NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# ==========================================================
# Streamlit Directory
# ==========================================================

STREAMLIT_DIR = BASE_DIR / "streamlit_app"

# ==========================================================
# Source Directory
# ==========================================================

SRC_DIR = BASE_DIR / "src"

# ==========================================================
# Global Configuration
# ==========================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

TARGET_COLUMN = "Next_Close"

DATE_COLUMN = "Date"

TICKER_COLUMN = "Ticker"

# ==========================================================
# Supported File Types
# ==========================================================

CSV_EXTENSION = ".csv"

MODEL_EXTENSION = ".pkl"

# ==========================================================
# Create Required Directories
# ==========================================================

DIRECTORIES = [

    RAW_DATA_DIR,

    PROCESSED_DATA_DIR,

    LIVE_DATA_DIR,

    MODELS_DIR,

    REPORTS_DIR,

    NOTEBOOKS_DIR,

    STREAMLIT_DIR

]

for directory in DIRECTORIES:

    directory.mkdir(
        parents=True,
        exist_ok=True
    )