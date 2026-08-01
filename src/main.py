from datetime import datetime

from fastapi import FastAPI, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.schemas import (
    ExpenseCreate,
    ExpenseResponse,
    ExpenseListResponse,
    SummaryAPIResponse,
)
from src.storage import (
    add_expense,
    calculate_total,
    delete_expense,
    get_category_distribution,
    get_dashboard_summary,
    get_expenses,
    get_recent_expenses,
    search_expenses,
)

app = FastAPI(
    title="💰 Smart Expense Tracker API",
    description="""
## Personal Expense Management API""",
    version="2.0.0",
    contact={
        "name": "Nithin M",
        "email": "your-email@gmail.com",
    },
    license_info={
        "name": "MIT License",
    },
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")


# ==========================================================
# Dashboard
# ==========================================================

@app.get(
    "/",
    response_class=HTMLResponse,
    tags=["Dashboard"],
    summary="Dashboard",
    description="Returns the Smart Expense Tracker dashboard."
)
def home(request: Request):

    dashboard = get_dashboard_summary()
    recent_expenses = get_recent_expenses()
    category_distribution = get_category_distribution()

    today = datetime.now().strftime("%d %b %Y")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "dashboard": dashboard,
            "recent_expenses": recent_expenses,
            "category_distribution": category_distribution,
            "today": today,
        },
    )


# ==========================================================
# Add Expense
# ==========================================================

@app.post(
    "/expenses",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Expense Management"],
    summary="Add a new expense",
    description="Create a new expense and store it in the JSON file.",
)
def create_expense(expense: ExpenseCreate):

    return add_expense(expense)


# ==========================================================
# Get Expenses
# ==========================================================

@app.get(
    "/expenses",
    response_model=ExpenseListResponse,
    tags=["Expense Management"],
    summary="View expenses",
    description="Returns all expenses or filters them by category.",
)
def list_expenses(
    category: str | None = Query(
        default=None,
        description="Filter by category"
    )
):

    expenses = get_expenses(category)

    return {
        "success": True,
        "message": "Expenses fetched successfully.",
        "count": len(expenses),
        "data": expenses,
    }


# ==========================================================
# Search Expenses
# ==========================================================

@app.get(
    "/expenses/search",
    response_model=ExpenseListResponse,
    tags=["Expense Management"],
    summary="Search expenses",
    description="Search expenses by title or category.",
)
def search_expense(
    query: str = Query(
        ...,
        min_length=1,
        description="Search keyword"
    )
):

    expenses = search_expenses(query)

    return {
        "success": True,
        "message": f"{len(expenses)} expense(s) found.",
        "count": len(expenses),
        "data": expenses,
    }


# ==========================================================
# Expense Summary
# ==========================================================

@app.get(
    "/expenses/summary",
    response_model=SummaryAPIResponse,
    tags=["Expense Management"],
    summary="Expense Summary",
    description="Returns the total expenses. Optionally filter by category.",
)
def expense_summary(
    category: str | None = Query(
        default=None,
        description="Category name"
    )
):

    return {
        "success": True,
        "message": "Summary generated successfully.",
        "data": {
            "total": calculate_total(category)
        },
    }


# ==========================================================
# Delete Expense
# ==========================================================

@app.delete(
    "/expenses/{expense_id}",
    tags=["Expense Management"],
    summary="Delete expense",
    description="Delete an expense using its unique ID.",
)
def remove_expense(expense_id: str):

    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found.",
        )

    return {
        "success": True,
        "message": "Expense deleted successfully.",
    }