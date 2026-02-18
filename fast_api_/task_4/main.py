import uvicorn
from fastapi import FastAPI, HTTPException, status
from models import Book

app = FastAPI()

# In-memory storage
books = []

# ---------------- CREATE BOOK ----------------
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    books.append(book)
    return book

# ---------------- GET ALL BOOKS ----------------
@app.get("/books")
def get_all_books():
    return books

# ---------------- GET BOOK BY ID ----------------
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# ---------------- DELETE BOOK ----------------
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)