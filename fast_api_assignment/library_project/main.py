import uvicorn
from fastapi import FastAPI
from database import Base, engine

from Books.router import router as book_router
from Members.router import router as member_router
from Loans.router import router as loan_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Production API")

app.include_router(book_router)
app.include_router(member_router)
app.include_router(loan_router)

@app.get("/")
def root():
    return {"message": "Library API Running"}

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)