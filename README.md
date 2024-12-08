# Book Management System

A simple Flask-based API for managing books. It supports CRUD operations, pagination, and token-based authentication.

## Setup

1. Clone the repository.
2. Install Python 3.9+.
3. Run:

python -m venv env source env/bin/activate # On Windows: env\Scripts\activate pip install flask

4. Start the server:
python app.py




## Features

- CRUD operations for books.
- Pagination.
- Search by title or author.
- Token-based authentication.

## API Endpoints

| Method | Endpoint            | Description         |
|--------|---------------------|---------------------|
| GET    | /books              | List all books      |
| POST   | /books              | Add a new book      |
| GET    | /books/<book_id>    | Get a book by ID    |
| PUT    | /books/<book_id>    | Update a book       |
| DELETE | /books/<book_id>    | Delete a book       |
| GET    | /search?query=<q>   | Search for books    |

## Testing

Run the tests:
python -m unittest discover -s tests 
