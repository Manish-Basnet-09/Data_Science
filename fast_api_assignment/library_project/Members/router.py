from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .schema import MemberCreate, MemberResponse
from .service import MemberService

router = APIRouter(prefix="/members", tags=["Members"])

@router.post("/", response_model=MemberResponse)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    return MemberService.create_member(db, member)

@router.get("/", response_model=list[MemberResponse])
def get_members(db: Session = Depends(get_db)):
    return MemberService.list_members(db)