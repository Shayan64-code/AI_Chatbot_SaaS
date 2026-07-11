from fastapi import APIRouter, UploadFile, File
import os
from services.pdf_services import extract_text
from utils.chunking import chunking
from utils.embeddings import embed_txt

router = APIRouter()

Upload_DIR = "./Backend/uploads"

@router.post("/uploads-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not os.path.exists(Upload_DIR):
        os.makedirs(Upload_DIR)

    File_Path = os.path.join(Upload_DIR, file.filename)

    with open(File_Path, "wb") as f:
        f.write(await f.read())

    #Text Extraction
    ext_txt = extract_text(File_Path)

    #Chunking
    chunks = chunking(text= ext_txt)

    #Embeddings
    embeddings = [embed_txt(chunk) for chunk in chunks]

    return {"message": "PDF uploaded successfully.", "file_name": file.filename}
        