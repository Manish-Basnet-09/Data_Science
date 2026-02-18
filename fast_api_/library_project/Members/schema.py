from pydantic import BaseModel, EmailStr

class MemberCreate(BaseModel):
    name: str
    email: EmailStr

class MemberResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True