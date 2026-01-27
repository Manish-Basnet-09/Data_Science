import uvicorn
from fastapi import FastAPI, HTTPException
from models import RegisterUser

app = FastAPI()

@app.post("/register")
def register(user: RegisterUser):

    # Custom validation logic
    if "password" in user.password.lower():
        raise HTTPException(
            status_code=400,
            detail="Password should not contain the word 'password'"
        )

    return {
        "message": "User registered successfully",
        "email": user.email
    }

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)