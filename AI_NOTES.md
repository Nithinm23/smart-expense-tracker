# AI_NOTES.md

# AI Usage Notes

This project was developed with the assistance of AI tools (ChatGPT), while the overall planning, implementation decisions, testing, and final review were completed by me.

---

## 1. Which parts were AI-assisted?

AI was mainly used as a development assistant during the implementation process.

It helped with:

- Discussing the overall project structure before coding.
- Selecting the technology stack (FastAPI, JSON storage, Pytest).
- Explaining how to set up the development environment.
- Generating initial versions of some API endpoints and helper functions.
- Suggesting cleaner implementations for certain functions.
- Improving code readability through refactoring.
- Explaining Python, FastAPI, and debugging concepts when errors occurred.
- Drafting the README.md and organizing project documentation.

---

## 2. What was done by me?

The overall design and implementation decisions were made by me.

My contributions include:

- Planning the project architecture and folder structure through discussions with AI.
- Deciding which features to implement based on the assignment requirements.
- Creating and organizing the project files.
- Integrating different modules into a working application.
- Debugging import errors, testing issues, and runtime problems.
- Modifying AI-generated code to improve readability and maintainability.
- Designing and improving the dashboard UI using HTML and CSS.
- Validating every API endpoint using Swagger UI.
- Running automated tests with Pytest and fixing issues until all tests passed.
- Reviewing the final project before submission.

---

## 3. What changes did I make to AI-generated code?

The initial AI-generated code was not used without review.

I made several modifications, including:

- Renaming variables and functions for better readability.
- Splitting logic into separate modules (storage, schemas, models, utils).
- Refactoring repeated code into reusable utility functions.
- Improving endpoint responses and Swagger documentation.
- Adding dashboard statistics and additional UI components.
- Enhancing the HTML and CSS layout for a cleaner user experience.
- Fixing import issues, validation errors, and JSON handling.
- Improving project organization and overall code consistency.

---

## 4. What AI suggestions were not used?

Some AI suggestions were intentionally not implemented.

Examples include:

- Using a database (SQLite or PostgreSQL). I kept JSON storage because the assignment explicitly stated that a database was not required.
- Adding authentication and user management. These features were outside the scope of the assignment.
- Adding Docker support. I chose to focus on completing the required functionality and the search bonus feature within the available time.

---

## 5. Validation Process

Every feature generated or suggested by AI was manually verified before being accepted.

Validation included:

- Testing each endpoint through Swagger UI.
- Verifying JSON storage behavior.
- Running the automated test suite.
- Fixing bugs found during development.
- Reviewing the final project structure and documentation.

The final project passed all automated tests successfully.
