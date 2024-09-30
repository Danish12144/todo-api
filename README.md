# FastAPI To-Do List API

A simple To-Do List API built with **FastAPI** and **SQLite**. This API allows users to create, read, update, and delete tasks in their to-do list.

## Features

- Create new to-do items
- Retrieve all to-do items
- Retrieve a specific to-do item by ID
- Update an existing to-do item
- Delete a to-do item

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python.
- **SQLAlchemy**: A SQL toolkit and ORM for Python.
- **SQLite**: A lightweight database for storing to-do items.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository or download the project files:

```bash
   git clone <repository-url>
   cd fastapi_todo
  python3 -m venv venv
  source venv/bin/activate
  pip install fastapi uvicorn sqlalchemy
  uvicorn main:app --reload
```
Create a to-do : `POST /todos/`
```json
{
  "title": "Task title",
  "description": "Task description"
}
```
Read all to-dos: `GET /todos/ `

Read a specific to-do :  `GET /todos/{todo_id}`

Update a to-do : `PUT /todos/{todo_id}`

Delete a to-do : `DELETE /todos/{todo_id}`

```json
{
  "title": "Updated title",
  "description": "Updated description"
}
```
