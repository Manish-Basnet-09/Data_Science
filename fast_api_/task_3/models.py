from pydantic import BaseModel

# 2. Student model (Pydantic)
class Student(BaseModel):
    name: str
    age: int
    course: str
