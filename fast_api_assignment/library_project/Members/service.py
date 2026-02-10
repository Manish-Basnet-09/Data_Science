from sqlalchemy.orm import Session
from .models import Member
from .schema import MemberCreate

class MemberService:

    @staticmethod
    def create_member(db: Session, data: MemberCreate):
        member = Member(**data.dict())
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def list_members(db: Session):
        return db.query(Member).all()