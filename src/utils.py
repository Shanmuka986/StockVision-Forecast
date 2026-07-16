"""
utils.py

Utility functions used throughout the StockVision Forecast V2 project.
"""

from pathlib import Path


def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    directory : Path
        Directory path to create.
    """
    directory.mkdir(parents=True, exist_ok=True)


def file_exists(file_path: Path) -> bool:
    """
    Check whether a file exists.

    Parameters
    ----------
    file_path : Path
        File path to check.

    Returns
    -------
    bool
        True if the file exists, otherwise False.
    """
    return file_path.exists()


def print_section(title: str) -> None:
    """
    Print a formatted section header.

    Parameters
    ----------
    title : str
        Section title.
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)