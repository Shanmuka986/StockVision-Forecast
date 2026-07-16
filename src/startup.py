"""
startup.py

Application startup initialization.

Runs all tasks that should execute when any
Streamlit page is opened.
"""

from src.accuracy import update_prediction_accuracy

# ==========================================================
# Startup Initialization
# ==========================================================

_initialized = False


def initialize_app():
    """
    Initialize application.

    This function is safe to call from every page.
    Startup tasks run only once per Python process.
    """

    global _initialized

    if _initialized:
        return

    print("=" * 60)
    print("Application Initialization")
    print("=" * 60)

    rows = update_prediction_accuracy()

    print(f"Predictions Verified : {rows}")

    print("=" * 60)
    print()

    _initialized = True