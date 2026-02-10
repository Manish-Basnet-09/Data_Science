from sqlalchemy.orm import Session
from .models import Loan
from .schema import LoanCreate

class LoanService:

    @staticmethod
    def create_loan(db: Session, data: LoanCreate):
        loan = Loan(**data.dict())
        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan

    @staticmethod
    def list_loans(db: Session):
        return db.query(Loan).all()