import uvicorn
from fastapi import FastAPI
from School.router import router as school_router
from Student.router import router as student_router  
from Teacher.router import router as teacher_router

#1.Create FastAPI instance
app = FastAPI()

#2.Define a root endpoint
@app.get("/")
def root():
    return {"message": "Hello World, Welcome to FastAPI!"} 

app.include_router(school_router)
app.include_router(student_router)
app.include_router(teacher_router)
# 3. Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)