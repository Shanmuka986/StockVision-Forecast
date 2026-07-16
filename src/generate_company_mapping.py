"""
generate_company_mapping.py

Generate company mapping from
trained tickers.
"""

import joblib
import yfinance as yf

from pathlib import Path

from src.config import MODELS_DIR


# ==========================================================
# Load Encoder
# ==========================================================

encoder = joblib.load(
    MODELS_DIR / "ticker_encoder.pkl"
)

tickers = sorted(
    encoder.classes_.tolist()
)

print(f"Total Companies : {len(tickers)}")

mapping = {}

# ==========================================================
# Download Company Names
# ==========================================================

for index, ticker in enumerate(tickers, start=1):

    print(
        f"[{index}/{len(tickers)}] {ticker}"
    )

    try:

        company = yf.Ticker(
            ticker
        )

        info = company.info

        name = info.get(
            "longName",
            ticker
        )

        mapping[ticker] = name

    except Exception:

        mapping[ticker] = ticker

# ==========================================================
# Save Mapping
# ==========================================================

output = Path(
    "src/company_mapping.py"
)

with open(
    output,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "COMPANY_MAPPING = {\n"
    )

    for ticker, company in mapping.items():

        company = company.replace(
            '"',
            '\\"'
        )

        file.write(
            f'    "{ticker}": "{company}",\n'
        )

    file.write("}\n")

print()

print("Company mapping saved successfully.")