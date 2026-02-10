from pydantic import BaseModel

class LoanCreate(BaseModel):
    book_title: str
    member_name: str

class LoanResponse(BaseModel):
    id: int
    book_title: str
    member_name: str

    class Config:
        from_attributes = True