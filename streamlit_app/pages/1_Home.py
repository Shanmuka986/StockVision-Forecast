"""
Home Page

StockVision Forecast V2
"""

import sys
from pathlib import Path
from datetime import datetime

import streamlit as st

# ==========================================================
# Add Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# ==========================================================
# Backend Imports
# ==========================================================

from src.predictor import predict_stock
from streamlit_app.utils import get_company_options
from streamlit_app.theme import render_theme_controls
from src.startup import initialize_app
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

    page_title="Home",

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

st.title("📈 StockVision Forecast V2")

st.markdown(
"""
### AI-Powered Stock Price Prediction

Predict the **next trading day's closing price**
using a Machine Learning model trained on
historical stock market data and powered by
**live Yahoo Finance data**.

Simply search for a company by **name** or
**stock ticker**, then generate a prediction
with a single click.
"""
)

st.success(
"""
🚀 **Placement Ready ML Project**

✔ Live Yahoo Finance
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ 472 Companies
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Machine Learning
&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
✔ Automatic Verification
"""
)

st.divider()
# ==========================================================
# Prediction Input
# ==========================================================

st.header("🔍 Select a Company")

st.write(
"""
Search using either the **company name** or the **stock ticker**
to generate a prediction for the next trading day's closing price.
"""
)

# ==========================================================
# Load Company List
# ==========================================================

company_options, reverse_mapping = get_company_options()

# ==========================================================
# Company Selection
# ==========================================================

selected_company = st.selectbox(

    label="Company",

    options=company_options,

    index=None,

    placeholder="🔍 Search by company name or ticker..."

)

# ==========================================================
# Selected Company
# ==========================================================

if selected_company:

    ticker = reverse_mapping[selected_company]

    st.success(
        f"✅ Selected Company: **{selected_company}**"
    )

else:

    ticker = None

    st.info(
        "👆 Select a company above to generate a prediction."
    )

st.divider()

# ==========================================================
# Prediction Button
# ==========================================================

predict_clicked = st.button(

    "🚀 Generate Prediction",

    width="stretch",

    disabled=(ticker is None)

)
# ==========================================================
# Generate Prediction
# ==========================================================

if predict_clicked:

    with st.spinner(
        "📥 Downloading latest market data and generating prediction..."
    ):

        try:

            # --------------------------------------------------
            # Predict Stock
            # --------------------------------------------------

            result = predict_stock(
                ticker
            )

            # --------------------------------------------------
            # Extract Prediction Values
            # --------------------------------------------------

            today_close = result["Today's Close"]

            predicted_close = result["Predicted Close"]

            change = result["Change"]

            change_percent = result["Change %"]

            direction = result["Direction"]

            prediction_time = datetime.now().strftime(
                "%d %b %Y %I:%M %p"
            )
                        # ==================================================
            # Prediction Generated
            # ==================================================

            st.divider()

            st.success(
                "✅ Prediction generated successfully."
            )

            # ==================================================
            # Prediction Results
            # ==================================================

            st.header("📊 Prediction Results")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(

                    label="💰 Today's Close",

                    value=f"${today_close:,.2f}"

                )

            with col2:

                st.metric(

                    label="🔮 Tomorrow's Prediction",

                    value=f"${predicted_close:,.2f}"

                )

            st.divider()

            # ==================================================
            # Forecast Summary
            # ==================================================

            col3, col4, col5 = st.columns(3)

            with col3:

                st.metric(

                    "📉 Price Change",

                    f"${change:,.2f}"

                )

            with col4:

                st.metric(

                    "📈 Expected Return",

                    f"{change_percent:.2f}%"

                )

            with col5:

                if direction == "UP":

                    st.success(
"""
### 🟢 BULLISH

Expected to Rise
"""
                    )

                else:

                    st.error(
"""
### 🔴 BEARISH

Expected to Fall
"""
                    )

            st.divider()
                        # ==================================================
            # Prediction Summary
            # ==================================================

            st.header("📝 Prediction Summary")

            company_name = selected_company.split(" (")[0]

            if direction == "UP":

                st.success(
f"""
**{company_name} ({ticker})** is expected to **increase**
by **${abs(change):.2f} ({abs(change_percent):.2f}%)**
during the next trading session.

The current Machine Learning model indicates a
**bullish short-term outlook** based on the latest
available market data.
"""
                )

            else:

                st.warning(
f"""
**{company_name} ({ticker})** is expected to **decrease**
by **${abs(change):.2f} ({abs(change_percent):.2f}%)**
during the next trading session.

The current Machine Learning model indicates a
**bearish short-term outlook** based on the latest
available market data.
"""
                )

            st.divider()

            # ==================================================
            # Market Insight
            # ==================================================

            st.header("📈 Market Insight")

            if direction == "UP":

                st.info(
"""
🟢 **Market Outlook: Positive**

The prediction suggests that the stock may continue
its short-term upward movement.

This forecast is generated using technical indicators
and historical market behaviour.
"""
                )

            else:

                st.info(
"""
🔴 **Market Outlook: Negative**

The prediction suggests that the stock may experience
a short-term downward movement.

This forecast is generated using technical indicators
and historical market behaviour.
"""
                )

            st.divider()

            # ==================================================
            # Disclaimer
            # ==================================================

            st.warning(
"""
⚠️ **Disclaimer**

This prediction is generated using a Machine Learning model
trained on historical stock market data.

It is intended for educational and research purposes only
and should **not** be considered financial or investment advice.
"""
            )

            st.caption(
                f"Prediction generated on **{prediction_time}**"
            )
                        # ==================================================
            # Footer
            # ==================================================

            st.divider()

            footer1, footer2, footer3 = st.columns(3)

            with footer1:

                st.caption(
f"""
**Prediction Time**

{prediction_time}
"""
                )

            with footer2:

                st.caption(
"""
**Machine Learning Model**

Linear Regression
"""
                )

            with footer3:

                st.caption(
"""
**Data Source**

Yahoo Finance
"""
                )

            st.divider()

            st.caption(
"""
© 2026 StockVision Forecast V2

Developed as a production-style Machine Learning application
for next trading day stock price forecasting using Python,
Scikit-Learn, Pandas, Streamlit and Yahoo Finance.
"""
            )

        except Exception as error:

            st.error(
                f"""
❌ Prediction Failed

{error}
"""
            )

            st.stop()