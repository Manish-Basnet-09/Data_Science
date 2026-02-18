import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from models import FileResponse

app = FastAPI()

@app.post("/upload-file", response_model=FileResponse)
async def upload_file(file: UploadFile = File(...)):

    # Allow only text and PDF files
    if file.content_type not in ["text/plain", "application/pdf"]:
        raise HTTPException(
            status_code=400,
            detail="Only text or PDF files are allowed"
        )

    contents = await file.read()
    
    file_size = len(contents)

    return {
        "filename": file.filename,
        "file_size": file_size
    }

# Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)