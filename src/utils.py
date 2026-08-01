"""
Utility functions used across the Smart Expense Tracker project.
"""

from uuid import uuid4
from pathlib import Path
import json
import logging

# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# -----------------------------
# UUID Generator
# -----------------------------
def generate_expense_id() -> str:
    """
    Generate a unique ID for every expense.
    """
    return str(uuid4())


# -----------------------------
# JSON Helper Functions
# -----------------------------
def read_json(file_path: Path):
    """
    Read JSON data from a file.
    Returns an empty list if the file is empty or invalid.
    """

    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        logger.warning("Invalid JSON detected. Resetting data file.")
        return []


def write_json(file_path: Path, data):
    """
    Write Python data into JSON format.
    """

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# API Response Helpers
# -----------------------------
def success_response(message: str, data=None):
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def error_response(message: str):
    return {
        "success": False,
        "message": message,
    }