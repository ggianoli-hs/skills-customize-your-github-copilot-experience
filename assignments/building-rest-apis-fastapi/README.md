# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small book-catalog REST API with FastAPI to practice defining data models, creating HTTP endpoints, and returning appropriate responses.

## 📝 Tasks

### 🛠️ Create the API and Book Model

#### Description
Set up the FastAPI application and define the data each book in the catalog will contain.

#### Requirements
Completed program should:

- Create a FastAPI application in `main.py`.
- Define a Pydantic model for a book with `title` and `author` fields.
- Store books in an in-memory collection, starting with at least two example books.

### 🛠️ Add Read Endpoints

#### Description
Create endpoints that let clients browse the catalog and look up a book by its ID.

#### Requirements
Completed program should:

- Add `GET /books` to return all books, including their IDs.
- Add `GET /books/{book_id}` to return one book.
- Return an HTTP 404 response when the requested book ID does not exist.

### 🛠️ Add a Create Endpoint

#### Description
Allow clients to add books to the catalog by sending JSON to the API.

#### Requirements
Completed program should:

- Add `POST /books` that accepts a book's title and author as a JSON request body.
- Use `next_book_id` to assign each new book a unique ID, then increment it.
- Add the new book to the in-memory collection.
- Return the created book with its ID and an HTTP 201 status.
- Run the API with `uvicorn main:app --reload` and use `/docs` to try each endpoint.

Install the required packages with `python -m pip install fastapi uvicorn` before running the API.
