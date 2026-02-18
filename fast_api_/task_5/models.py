from pydantic import BaseModel, EmailStr, Field

class RegisterUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)