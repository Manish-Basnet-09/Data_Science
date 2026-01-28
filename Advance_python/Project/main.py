import uvicorn
from fastapi import FastAPI, HTTPException
import pandas as pd
   

app = FastAPI(title="Employee Data API")


# Load cleaned data once at startup
employees_df = pd.read_csv("clean_employee_data.csv")

@app.get("/employees")
def get_employees():
    return employees_df.to_dict(orient="records")

# Get employee by Name
@app.get("/employees/{emp_id}")
def get_employee_by_id(emp_id: int):
    employee = employees_df[employees_df["Id"] == emp_id]

    if employee.empty:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee.to_dict(orient="records")[0]



# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)