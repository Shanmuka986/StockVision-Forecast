"""
Live Data

StockVision Forecast V2
"""

import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# ==========================================================
# Imports
# ==========================================================

import pandas as pd
import streamlit as st

from src.config import LIVE_DATA_DIR
from src.company_mapping import COMPANY_MAPPING
from src.startup import initialize_app
from streamlit_app.theme import render_theme_controls
# ==========================================================
# Load CSS
# ==========================================================

css_file = (

    PROJECT_ROOT

    / "streamlit_app"

    / "assets"

    / "styles.css"

)

if css_file.exists():

    with open(css_file) as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Live Data",

    page_icon="📈",

    layout="wide"

)
# ==========================================================
# Application Startup
# ==========================================================

initialize_app()

with st.sidebar:

    render_theme_controls()

# ==========================================================
# Hero Section
# ==========================================================

st.title("📈 Live Stock Data")

st.markdown(
"""
### Live Market Data Explorer

Browse and explore the historical stock market datasets
downloaded from **Yahoo Finance**.

Search by **company name** or **stock ticker**, preview
the downloaded data, inspect available features and
download datasets for further analysis.
"""
)

st.success(
"""
📊 **Live Dataset Explorer**

✔ Yahoo Finance
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Company Search
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Dataset Preview
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ CSV Download
"""
)

st.divider()

# ==========================================================
# Load CSV Files
# ==========================================================

csv_files = sorted(

    LIVE_DATA_DIR.glob("*.csv"),

    reverse=True

)

if not csv_files:

    st.warning(

        """
No live datasets found.

Generate a prediction first to download live data.
        """

    )

    st.stop()
# ==========================================================
# Live Dataset Overview
# ==========================================================

latest_file = csv_files[0]

# Read the latest trading day from the dataset
latest_dataset = pd.read_csv(latest_file)

if "Date" in latest_dataset.columns:

    latest_date = str(
        latest_dataset["Date"].iloc[-1]
    )[:10]

else:

    latest_date = "-"

# ----------------------------------------------------------
# Load Latest Dataset
# ----------------------------------------------------------

latest_dataset = pd.read_csv(latest_file)

if "Close" in latest_dataset.columns:

    latest_close = latest_dataset["Close"].iloc[-1]

    latest_close_text = f"${latest_close:,.2f}"

else:

    latest_close_text = "-"

# ----------------------------------------------------------
# Summary Cards
# ----------------------------------------------------------

card1, card2, card3, card4 = st.columns(4)

with card1:

    st.metric(

        "📂 Available Datasets",

        len(csv_files)

    )

with card2:

    st.metric(

        "🏢 Supported Companies",

        len(COMPANY_MAPPING)

    )

with card3:

    st.metric(

        "📅 Latest Dataset",

        latest_date

    )

with card4:

    st.metric(

        "💰 Latest Close Price",

        latest_close_text

    )

st.divider()

# ==========================================================
# Search & Dataset Selection
# ==========================================================

st.header("🔍 Find a Dataset")

st.write(
"""
Search for a downloaded dataset using the **company name**
or **stock ticker**, then select it to preview the
historical market data.
"""
)

# ----------------------------------------------------------
# Search Dataset
# ----------------------------------------------------------

search = st.text_input(

    label="Search",

    placeholder="🔍 Search by company name or ticker..."

)

filtered_files = []

# ----------------------------------------------------------
# Filter Files
# ----------------------------------------------------------

if search:

    for file in csv_files:

        ticker = file.stem.upper()

        company = COMPANY_MAPPING.get(
            ticker,
            ticker
        )

        if (

            search.lower() in ticker.lower()

            or

            search.lower() in company.lower()

        ):

            filtered_files.append(file)

else:

    filtered_files = csv_files

# ----------------------------------------------------------
# No Match
# ----------------------------------------------------------

if not filtered_files:

    st.warning(
        "No matching dataset found."
    )

    st.stop()

# ==========================================================
# Dataset Selection
# ==========================================================

dataset_options = {}

for file in filtered_files:

    ticker = file.stem.upper()

    company = COMPANY_MAPPING.get(
        ticker,
        ticker
    )

    dataset_options[
        f"{company} ({ticker})"
    ] = file

selected_dataset = st.selectbox(

    "Dataset",

    list(dataset_options.keys())

)

selected_file = dataset_options[selected_dataset]

st.success(
    f"✅ Selected Dataset: **{selected_dataset}**"
)

st.divider()
# ==========================================================
# Load Selected Dataset
# ==========================================================

data = pd.read_csv(selected_file)
# ==========================================================
# Dataset Information
# ==========================================================

st.header("📊 Dataset Information")

# ----------------------------------------------------------
# Latest Trading Day
# ----------------------------------------------------------

if "Date" in data.columns:

    latest_record = str(
        data["Date"].iloc[-1]
    )[:10]

else:

    latest_record = "-"

# ----------------------------------------------------------
# Latest Closing Price
# ----------------------------------------------------------

if "Close" in data.columns:

    latest_close = f"${data['Close'].iloc[-1]:,.2f}"

else:

    latest_close = "-"

# ----------------------------------------------------------
# Information Cards
# ----------------------------------------------------------

card1, card2, card3, card4 = st.columns(4)

with card1:

    st.metric(
        "📄 Total Records",
        len(data)
    )

with card2:

    st.metric(
        "📑 Features",
        len(data.columns)
    )

with card3:

    st.metric(
        "📅 Latest Trading Day",
        latest_record
    )

with card4:

    st.metric(
        "💰 Latest Close",
        latest_close
    )

st.divider()

# ==========================================================
# Dataset Preview
# ==========================================================

st.header("📋 Dataset Preview")

st.write(
"""
Preview the downloaded Yahoo Finance dataset
before downloading or analyzing it.
"""
)

preview_option = st.radio(

    "Display",

    [

        "Latest 10 Rows",

        "First 10 Rows"

    ],

    horizontal=True

)

if preview_option == "Latest 10 Rows":

    preview = data.tail(10)

else:

    preview = data.head(10)

st.dataframe(

    preview,

    width="stretch",

    hide_index=True

)

st.divider()

# ==========================================================
# Available Columns
# ==========================================================

st.header("📑 Available Features")

column_df = pd.DataFrame(

    {

        "No.": range(

            1,

            len(data.columns) + 1

        ),

        "Feature": data.columns

    }

)

st.dataframe(

    column_df,

    width="stretch",

    hide_index=True

)

st.divider()
# ==========================================================
# Download Dataset
# ==========================================================

st.header("⬇ Download Dataset")

st.write(
"""
Download the selected Yahoo Finance dataset
for offline analysis or further Machine Learning
experiments.
"""
)

st.download_button(

    label="📥 Download Selected Dataset",

    data=data.to_csv(index=False),

    file_name=selected_file.name,

    mime="text/csv",

    width="stretch"

)

st.divider()

# ==========================================================
# Dataset Columns
# ==========================================================

st.header("📑 Available Columns")

column_df = pd.DataFrame(

    {

        "Column Number": range(

            1,

            len(data.columns) + 1

        ),

        "Column Name": data.columns

    }

)

st.dataframe(

    column_df,

    width="stretch",

    hide_index=True

)

st.divider()

# ==========================================================
# Dataset Statistics
# ==========================================================

with st.expander(
    "📈 View Dataset Statistics"
):

    st.write(
"""
The statistics below summarize the numerical
features contained in the selected dataset.
"""
    )

    numeric_columns = data.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) > 0:

        st.dataframe(

            data[numeric_columns]

            .describe()

            .T,

            width="stretch"

        )

    else:

        st.info(
            "No numeric columns available."
        )

st.divider()

# ==========================================================
# Footer
# ==========================================================

footer1, footer2, footer3 = st.columns(3)

with footer1:

    st.caption(
"""
**Module**

Live Data Explorer
"""
    )

with footer2:

    st.caption(
"""
**Data Source**

Yahoo Finance
"""
    )

with footer3:

    st.caption(
"""
**Supported Companies**

472
"""
    )

st.divider()

st.caption(
"""
© 2026 StockVision Forecast V2

Historical datasets are automatically downloaded
from Yahoo Finance and used for Machine Learning
feature engineering and prediction.

This module allows users to inspect, preview and
download the datasets used by the application.
"""
)