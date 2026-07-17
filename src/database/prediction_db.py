"""
Database Operations
StockVision Forecast V2.1
"""

from psycopg.rows import dict_row

from src.database.connection import get_connection
from src.database.schema import TABLE_NAME


def save_prediction(
    prediction_id,
    prediction_date,
    target_trading_date,
    ticker,
    company_name,
    today_close,
    predicted_close,
):
    """
    Save a new prediction into PostgreSQL.
    """

    query = f"""
        INSERT INTO {TABLE_NAME}
        (
            prediction_id,
            prediction_date,
            target_trading_date,
            ticker,
            company_name,
            today_close,
            predicted_close,
            prediction_status
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    conn = get_connection()

    try:

        with conn.cursor() as cur:

            cur.execute(
                query,
                (
                    prediction_id,
                    prediction_date,
                    target_trading_date,
                    ticker,
                    company_name,
                    today_close,
                    predicted_close,
                    "Pending",
                ),
            )

        conn.commit()

    finally:

        conn.close()


def get_prediction_history():
    """
    Return all predictions.
    """

    conn = get_connection()

    try:

        with conn.cursor(row_factory=dict_row) as cur:

            cur.execute(
                f"""
                SELECT *
                FROM {TABLE_NAME}
                ORDER BY prediction_date DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()


def get_pending_predictions():
    """
    Return all pending predictions.
    """

    conn = get_connection()

    try:

        with conn.cursor(row_factory=dict_row) as cur:

            cur.execute(
                f"""
                SELECT *
                FROM {TABLE_NAME}
                WHERE prediction_status='Pending'
                ORDER BY prediction_date
                """
            )

            return cur.fetchall()

    finally:

        conn.close()


def update_prediction(
    prediction_id,
    actual_close,
):
    """
    Update prediction after verification.
    """

    conn = get_connection()

    try:

        with conn.cursor() as cur:

            cur.execute(
                f"""
                UPDATE {TABLE_NAME}
                SET
                    actual_close=%s,
                    prediction_status='Verified',
                    updated_at=CURRENT_TIMESTAMP
                WHERE prediction_id=%s
                """,
                (
                    actual_close,
                    prediction_id,
                ),
            )

        conn.commit()

    finally:

        conn.close()