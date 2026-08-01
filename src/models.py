from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    "model representing an expense"

    id: str
    title: str
    amount: float
    category: str
    date: date