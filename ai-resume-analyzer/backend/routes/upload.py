from fastapi import APIRouter, UploadFile
from utils.file_handler import extract_text

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    text = await extract_text(file)
    return {"text": text}
