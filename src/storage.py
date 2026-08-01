from pathlib import Path
from datetime import date
from typing import List, Optional
from collections import defaultdict
from collections import defaultdict
from src.models import Expense
from src.schemas import ExpenseCreate
from src.utils import (
    generate_expense_id,
    read_json,
    write_json,
    logger,
)

DATA_FILE = Path(__file__).parent / "data.json"


def load_expenses() -> List[Expense]:
    "Load all expenses from json"

    raw_data = read_json(DATA_FILE)

    expenses = []

    for item in raw_data:
        expenses.append(
            Expense(
                id=item["id"],
                title=item["title"],
                amount=item["amount"],
                category=item["category"],
                date=date.fromisoformat(item["date"]),
            )
        )

    return expenses


def save_expenses(expenses: List[Expense]) -> None:
    "Saving all expenses into json"
    data = []

    for expense in expenses:
        data.append(
            {
                "id": expense.id,
                "title": expense.title,
                "amount": expense.amount,
                "category": expense.category,
                "date": expense.date.isoformat(),
            }
        )

    write_json(DATA_FILE, data)


def add_expense(expense: ExpenseCreate) -> Expense:
    "Creating new expense and save to json file"
    expenses = load_expenses()

    new_expense = Expense(
        id=generate_expense_id(),
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
    )

    expenses.append(new_expense)

    save_expenses(expenses)

    logger.info("Expense added: %s", new_expense.title)

    return new_expense


def get_expenses(category: Optional[str] = None) -> List[Expense]:
    "Return all expenses or filtering by category"
    expenses = load_expenses()

    if category:

        expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

    return expenses


def delete_expense(expense_id: str) -> bool:
    "Delete expense using IDs"
    expenses = load_expenses()

    remaining = [
        expense
        for expense in expenses
        if expense.id != expense_id
    ]

    if len(remaining) == len(expenses):
        logger.warning("Expense not found: %s", expense_id)
        return False

    save_expenses(remaining)

    logger.info("Expense deleted: %s", expense_id)

    return True


def calculate_total(category: Optional[str] = None) -> float:
    "From the expenses, calculate total amount"
    expenses = get_expenses(category)

    total = sum(expense.amount for expense in expenses)

    return round(total, 2)


def total_expense_count() -> int:
    "Return total number of expenses"
    return len(load_expenses())
def get_total_categories() -> int:
    """
    Return the number of unique expense categories.
    """

    expenses = load_expenses()

    categories = {
        expense.category.lower()
        for expense in expenses
    }

    return len(categories)


def get_dashboard_summary() -> dict:
    """
    Return dashboard statistics.
    """

    expenses = load_expenses()

    return {
        "expense_count": len(expenses),
        "total_amount": round(
            sum(expense.amount for expense in expenses),
            2
        ),
        "category_count": len(
            {
                expense.category.lower()
                for expense in expenses
            }
        ),
    }


def get_recent_expenses(limit: int = 5):
    """
    Return the most recent expenses.
    """

    expenses = load_expenses()

    expenses.sort(
        key=lambda expense: expense.date,
        reverse=True
    )

    return expenses[:limit]
def get_category_distribution() -> dict:
    """
    Returns the total amount spent in each category.
    """

    expenses = load_expenses()

    category_total = defaultdict(float)

    for expense in expenses:
        category_total[expense.category] += expense.amount

    return dict(category_total)
def search_expenses(query: str) -> List[Expense]:
    """
    Search expenses by title or category.
    """

    expenses = load_expenses()

    query = query.lower().strip()

    return [
        expense
        for expense in expenses
        if query in expense.title.lower()
        or query in expense.category.lower()
    ]