import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import crud
from database import engine, get_db
from schemas import UserCreate, UserResponse

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create user
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Get all users
@app.get("/users/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)