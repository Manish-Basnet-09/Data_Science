from sqlalchemy import Column, Integer, String
from database import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String)
    member_name = Column(String)