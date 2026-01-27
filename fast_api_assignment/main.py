import uvicorn
from fastapi import FastAPI
from typing import Optional 
# 1. Create the App instance
app = FastAPI()

# 2. Define a Path Operation (Route)
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int, active: Optional[bool] = None):
    return {
        "user_id": user_id,
        "active": active
    }

# 3. Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)

