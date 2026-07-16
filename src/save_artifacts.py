"""
Generate deployment artifacts
without retraining the model.
"""

import json
import joblib
import pandas as pd

from src.config import (
    MODELS_DIR,
    PROCESSED_DATA_DIR,
)


def main():

    print("=" * 60)
    print("Generating Deployment Artifacts")
    print("=" * 60)

    X_train = pd.read_csv(
        PROCESSED_DATA_DIR / "X_train.csv"
    )

    feature_columns = list(X_train.columns)

    joblib.dump(
        feature_columns,
        MODELS_DIR / "feature_columns.pkl"
    )

    print("✓ feature_columns.pkl saved")

    metrics = {

        "Model": "Linear Regression",

        "MAE": 2.3434,

        "RMSE": 5.9730,

        "MAPE": 0.0138,

        "R2 Score": 0.9995

    }

    with open(
        MODELS_DIR / "metrics.json",
        "w"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4
        )

    print("✓ metrics.json saved")

    model_info = {

        "Project": "StockVision Forecast V2",

        "Model": "Linear Regression",

        "Target": "Next_Close",

        "Number of Features": len(feature_columns),

        "Version": "2.0"

    }

    with open(
        MODELS_DIR / "model_info.json",
        "w"
    ) as file:

        json.dump(
            model_info,
            file,
            indent=4
        )

    print("✓ model_info.json saved")

    print()
    print("=" * 60)
    print("All deployment artifacts generated.")
    print("=" * 60)


if __name__ == "__main__":

    main()