from datetime import date
from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    "Schema for creating new expense"
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Title of the expense"
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount (must be greater than zero)"
    )

    category: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Expense category"
    )

    date: date


class ExpenseResponse(ExpenseCreate):
    "schema for returning expense data from API"
    id: str

class SummaryResponse(BaseModel):
    total: float

class APIResponse(BaseModel):
    """
    Standard API response.
    """

    success: bool
    message: str


class ExpenseListResponse(APIResponse):
    """
    Response returned when listing expenses.
    """

    count: int
    data: list[ExpenseResponse]


class SummaryAPIResponse(APIResponse):
    """
    Response returned for summary endpoint.
    """

    data: SummaryResponse