from pydantic import BaseModel

class FileResponse(BaseModel):
    filename: str
    file_size: int