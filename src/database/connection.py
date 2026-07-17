"""
Database Connection
StockVision Forecast V2.1
"""

import os

import psycopg
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_secret(key):
    """Read from Streamlit secrets first, then fall back to .env."""
    if key in st.secrets:
        return st.secrets[key]
    return os.getenv(key)


def get_connection():
    """Return PostgreSQL database connection."""

    return psycopg.connect(
        host=get_secret("DB_HOST"),
        port=get_secret("DB_PORT"),
        dbname=get_secret("DB_NAME"),
        user=get_secret("DB_USER"),
        password=get_secret("DB_PASSWORD"),
    )