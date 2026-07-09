# Library API

A simple RESTful Library Management API built with **FastAPI**, **SQLModel**, **PostgreSQL**, and **Docker**.

## Features

- Create book records
- Retrieve all books
- Retrieve a book by ID
- Search books by title or author
- Update book details
- Create book categories
- Store data in a PostgreSQL database

## Technologies Used

- Python 3
- FastAPI
- SQLModel
- PostgreSQL
- Docker
- Uvicorn

## Project Structure

```
library-api/
│── database/
│   ├── __init__.py
│   └── session.py
│
│── models/
│   ├── __init__.py
│   ├── book.py
│   └── category.py
│
│── main.py
│── docker-compose.yml
│── .env
│── .gitignore
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome message |
| POST | /categories | Create a category |
| POST | /books | Create a new book |
| GET | /books | List all books |
| GET | /books/search | Search books by title or author |
| GET | /books/{book_id} | Retrieve a book by ID |
| PATCH | /books/{book_id} | Update a book |

## Running the Project

1. Clone the repository.

```bash
git clone https://github.com/zanzikuria-create/library-api.git
```

2. Navigate to the project folder.

```bash
cd library-api
```

3. Start PostgreSQL using Docker.

```bash
docker compose up -d
```

4. Run the FastAPI application.

```bash
uvicorn main:app --reload
```

5. Open Swagger UI.

```
http://127.0.0.1:8000/docs
```

## Author

**Mildred Kuria**

Computer Science Student

Built as part of a Backend Development Lab using FastAPI, SQLModel, PostgreSQL, and Docker.

