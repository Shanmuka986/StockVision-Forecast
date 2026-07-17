"""
Database Table Configuration
StockVision Forecast V2.1
"""

TABLE_NAME = "prediction_history"

COLUMNS = {
    "prediction_id": "prediction_id",
    "prediction_date": "prediction_date",
    "target_trading_date": "target_trading_date",
    "ticker": "ticker",
    "company_name": "company_name",
    "today_close": "today_close",
    "predicted_close": "predicted_close",
    "actual_close": "actual_close",
    "prediction_status": "prediction_status",
}