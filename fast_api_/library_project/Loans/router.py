from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .schema import LoanCreate, LoanResponse
from .service import LoanService

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", response_model=LoanResponse)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    return LoanService.create_loan(db, loan)

@router.get("/", response_model=list[LoanResponse])
def get_loans(db: Session = Depends(get_db)):
    return LoanService.list_loans(db)