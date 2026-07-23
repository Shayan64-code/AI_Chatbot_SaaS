from fastapi import APIRouter, UploadFile, File

from services.pdf_services import process_pdf

router = APIRouter()

@router.post("/uploads-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
     """
     Upload and process pdf
     """
     return await process_pdf(file)