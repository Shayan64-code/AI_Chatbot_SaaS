from fastapi import APIRouter, UploadFile, File
import os
from services.pdf_services import extract_text
from utils.chunking import chunking
from utils.embeddings import embed_txt
from utils.file_utils import generate_hash_code

router = APIRouter()

Upload_DIR = "./Backend/uploads"

@router.post("/uploads-pdf/")
async def upload_pdf(file: UploadFile = File(...)):

    file_bytes = await file.read()
    file_hash = generate_hash_code(file_bytes)

    #Checking hash Duplicate
    processed_hash = set()  #Change with Vector DB
    if file_hash in processed_hash():
        return {"message": "File is already processed", "hash": file_hash}

    #Save file
    if not os.path.exists(Upload_DIR):
        os.makedirs(Upload_DIR)
    File_Path = os.path.join(Upload_DIR, file.filename)
    with open(File_Path, "wb") as f:
        f.write(file_bytes)

    #Text Extraction
    ext_txt = extract_text(File_Path)

    #Chunking
    chunks = chunking(text=ext_txt)

    #Embeddings
    embeddings = [embed_txt(chunk) for chunk in chunks]

    #Later Replace with vector DB
    processed_hash.add(file_hash)

    return {"message": "PDF uploaded successfully.", 
            "file_name": file.filename,
            "hash": file_hash,
            "chunks_count": len(chunks),
            "sample_chunk": chunks[0][:200] if chunks else None}
        