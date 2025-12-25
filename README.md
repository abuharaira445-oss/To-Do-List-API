# To-Do-List-API
A simple and clean RESTful To-Do List API built using Python, FastAPI, and SQLite.
This project demonstrates basic CRUD operations, database integration, and API development using FastAPI.

# Features

* Create, read, update, and delete tasks (CRUD)
* SQLite database for persistent storage
* FastAPI for high-performance API
* Automatic API documentation (Swagger UI)
* Simple and beginner-friendly project structure

# Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn

# Project Structure

todo-api/
│
├── main.py          # FastAPI app & routes
├── database.py      # SQLite connection & table creation
├── models.py        # Pydantic models
├── todo.db          # SQLite database
├── requirements.txt
└── README.md

# API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | /tasks        | Get all tasks           |
| GET    | /tasks/{id}   | Get task by ID          |
| POST   |  /tasks       | Create a new task       |
| PUT    |  /tasks/{id}  | Update an existing task |
| DELETE |  /tasks/{id}  | Delete a task           |

---

# Example Task Model

{
  "title": "Learn FastAPI",
  "description": "Build a To-Do API",
  "status": "pending"
}

# Purpose

This project is designed to:

* Practice FastAPI fundamentals
* Learn SQLite database integration
* Understand RESTful API development
* Build a strong foundation for larger backend projects

# Author

Abu Huraira
Learning backend development with FastAPI & Python 
