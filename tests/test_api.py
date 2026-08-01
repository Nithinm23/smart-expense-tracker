import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

DATA_FILE = Path("src/data.json")


def reset_database():
    """
    Reset the JSON file before each test.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200


def test_add_expense():

    reset_database()

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 500,
            "category": "Food",
            "date": "2026-08-01",
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == "Pizza"

    assert body["amount"] == 500

    assert body["category"] == "Food"


def test_get_all_expenses():

    reset_database()

    client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 120,
            "category": "Food",
            "date": "2026-08-01",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    assert body["count"] == 1


def test_filter_by_category():

    reset_database()

    client.post(
        "/expenses",
        json={
            "title": "Petrol",
            "amount": 800,
            "category": "Transport",
            "date": "2026-08-01",
        },
    )

    response = client.get("/expenses?category=Transport")

    body = response.json()

    assert body["count"] == 1

    assert body["data"][0]["category"] == "Transport"


def test_search_expense():

    reset_database()

    client.post(
        "/expenses",
        json={
            "title": "Netflix",
            "amount": 649,
            "category": "Entertainment",
            "date": "2026-08-01",
        },
    )

    response = client.get("/expenses/search?query=Netflix")

    body = response.json()

    assert response.status_code == 200

    assert body["count"] == 1


def test_summary():

    reset_database()

    client.post(
        "/expenses",
        json={
            "title": "Electricity",
            "amount": 1800,
            "category": "Bills",
            "date": "2026-08-01",
        },
    )

    response = client.get("/expenses/summary")

    body = response.json()

    assert response.status_code == 200

    assert body["data"]["total"] == 1800


def test_delete_expense():

    reset_database()

    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 150,
            "category": "Food",
            "date": "2026-08-01",
        },
    )

    expense_id = response.json()["id"]

    delete = client.delete(f"/expenses/{expense_id}")

    assert delete.status_code == 200

    assert delete.json()["success"] is True


def test_invalid_amount():

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": -10,
            "category": "Food",
            "date": "2026-08-01",
        },
    )

    assert response.status_code == 422