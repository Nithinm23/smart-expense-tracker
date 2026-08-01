# 🧪 Testing

The project includes an automated test suite written using **Pytest** to verify the functionality of the REST API.

The tests validate both successful operations and input validation to ensure the application behaves as expected.

## Test Coverage

The following API features are tested:

| Test Case | Description |
|-----------|-------------|
| ✅ Home Page | Verifies the dashboard loads successfully. |
| ✅ Add Expense | Confirms a new expense can be created successfully. |
| ✅ View Expenses | Ensures all stored expenses are returned correctly. |
| ✅ Filter by Category | Verifies category-based filtering works as expected. |
| ✅ Search Expenses | Confirms searching by title or category returns matching expenses. |
| ✅ Expense Summary | Verifies total expense calculation. |
| ✅ Delete Expense | Ensures an expense can be deleted successfully. |
| ✅ Invalid Input | Confirms validation rejects invalid expense data (e.g., negative amount). |

---

## Running the Tests

Run the following command from the project root:

```bash
pytest -v
```

Expected result:

```text
=========================================
8 passed
=========================================
```

The complete test suite validates all major API endpoints and ensures that the application behaves correctly under normal and invalid input conditions.

---

## Test Screenshot

