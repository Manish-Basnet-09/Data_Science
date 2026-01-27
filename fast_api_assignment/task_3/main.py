import uvicorn
from fastapi import FastAPI
from models import Student

# 1. Create the App instance
app = FastAPI()


# 2. POST endpoint
@app.post("/students")
def create_student(student: Student):
    return student


# 3. Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
