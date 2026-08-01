# 💰 Smart Expense Tracker API

![Python](https://img.shields.io/badge<img width="948" height="433" alt="Screenshot 2026-08-01 135231" src="https://github.com/user-attachments/assets/edd3641a-ee5d-495e-9dc4-bb654ca9d736" />
/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Pytest](https://img.shields.io/badge/Tests-8_Passed-success)
![License](https://img.shields.io/badge/License-MIT-orange)

A modern REST API built with **FastAPI** for managing personal expenses. The application provides a clean REST API, an interactive dashboard, automated tests, and JSON-based storage without requiring a database.

---

# 📸 Dashboard

> Replace the image paths below with your screenshots after uploading them to the **images/** folder.

![Dashboard](<img width="948" height="433" src="https://github.com/user-attachments/assets/d8b3fcee-7bfa-4cfa-aa7c-ac481ca3fdd6" />)

---

# 📌 Project Overview

Smart Expense Tracker is a lightweight expense management application that enables users to manage their daily expenses efficiently.

The project was developed using **FastAPI** with a layered architecture to keep the code clean, maintainable, and easy to extend.

The application stores data locally in a **JSON file**, making it lightweight while still demonstrating REST API design principles.

---

# ✨ Features

## Core Features

- ✅ Add New Expense
- ✅ View All Expenses
- ✅ Filter Expenses by Category
- ✅ Calculate Expense Summary
- ✅ Delete Expense

## Bonus Feature

- 🔍 Search Expenses by Title or Category

## Dashboard

- 📊 Total Expenses
- 💰 Total Expense Amount
- 📂 Category Count
- 📅 Current Date
- 📑 Recent Expenses
- 📈 Expense Distribution
- ⚡ Quick Actions
- 🟢 API Information Panel

## Additional Features

- Interactive Swagger Documentation
- Responsive Dashboard
- JSON File Storage
- Layered Project Structure
- Automated Unit Testing

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3.14 | Programming Language |
| FastAPI | REST API Framework |
| Jinja2 | HTML Templates |
| HTML5 | Frontend |
| CSS3 | Styling |
| JSON | Local Storage |
| Pytest | Automated Testing |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```text
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── pytest.ini
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── storage.py
│   ├── utils.py
│   ├── data.json
│   │
│   ├── static/
│   │     └── style.css
│   │
│   └── templates/
│         └── index.html
│
├── tests/
│     └── test_api.py
│
└── images/
      ├── dashboard.png
      ├── swagger.png
      └── tests.png
```

---

# 🏗 Project Workflow

```text
                Client Request
                      │
                      ▼
               FastAPI Endpoints
                      │
                      ▼
             Business Logic Layer
                (storage.py)
                      │
                      ▼
             JSON File Storage
               (data.json)
                      │
                      ▼
               API Response
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YourUsername/smart-expense-tracker.git
```

```bash
cd smart-expense-tracker
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
uvicorn src.main:app --reload
```

Application will be available at

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Dashboard |
| POST | /expenses | Add Expense |
| GET | /expenses | View All Expenses |
| GET | /expenses?category=Food | Filter by Category |
| GET | /expenses/search?query=Pizza | Search Expenses |
| GET | /expenses/summary | Expense Summary |
| DELETE | /expenses/{expense_id} | Delete Expense |

---

# 📊 Example Request

## Add Expense

```json
{
  "title": "Domino's Pizza",
  "amount": 650,
  "category": "Food",
  "date": "2026-08-01"
}
```

---

## Example Response

```json
{
  "title": "Domino's Pizza",
  "amount": 650,
  "category": "Food",
  "date": "2026-08-01",
  "id": "e7c97d56-4fd4-41e0-a5d1-7d2b2b78c991"
}
```

---

# 🧪 Running Tests

Run the complete test suite

```bash
pytest -v
```

Expected Output

```text
==================================
8 passed
==================================
```

---

# 📸 Screenshots

## Dashboard

![Dashboard](images/dashboard.png)

---

## Swagger Documentation

![Swagger](images/swagger.png)

---

## Test Results

![Tests](images/tests.png)

---

# 🎯 Design Decisions

This project follows a simple layered architecture.

- Business logic is separated into a dedicated storage layer.
- Utility functions are reused across the application.
- Pydantic models validate incoming requests.
- JSON is used instead of a database to keep deployment simple.
- Interactive Swagger documentation improves API usability.
- Automated tests verify all major API endpoints.

---

# 🔮 Future Improvements

- SQLite / PostgreSQL Integration
- User Authentication
- Expense Update API
- Monthly Reports
- Data Visualization Charts
- Docker Support
- CI/CD Pipeline
- Cloud Deployment

---

# 👨‍💻 Author

**Nithin M**

Electronics & Communication Engineering

Machine Learning | Computer Vision | Backend Development

GitHub:
https://github.com/Nithinm23

---

# 📄 License

This project was developed as part of the **Software Engineering Apprenticeship Assignment (2026)**.

Licensed under the **MIT License**.

---

⭐ If you found this project useful, feel free to star the repository.
