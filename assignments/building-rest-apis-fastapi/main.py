from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(title="A Wrinkle in Time", author="Madeleine L'Engle"),
}
next_book_id = max(books) + 1


@app.get("/books")
def list_books():
    # TODO: Return every book with its ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the requested book, or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Assign a unique ID, store the book, and return it with its ID.
    pass
