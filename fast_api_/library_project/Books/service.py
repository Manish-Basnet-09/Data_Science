from sqlalchemy.orm import Session
from .models import Book
from .schema import BookCreate

class BookService:

    @staticmethod
    def create_book(db: Session, data: BookCreate):
        book = Book(**data.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def list_books(db: Session):
        return db.query(Book).all()