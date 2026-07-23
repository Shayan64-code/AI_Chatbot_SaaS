import os
import fitz
from typing import List

from fastapi import UploadFile

from services.vector_services import VectorService

from utils.chunking import chunking
from utils.embeddings import embedding_documents
from utils.file_utils import generate_hash_code


UPLOAD_DIR = "./Backend/uploads"

###Save File
def save_pdf(file_name: str, file_bytes: bytes) -> str:
    """
    Save the uploaded PDF to disk.

    Returns:
        str: Saved file path.
    """

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_DIR,
        file_name
    )

    with open(file_path, "wb") as pdf_file:
        pdf_file.write(file_bytes)

    return file_path

###Extract text
def extract_text(file_path: str) -> str:
    """
    Extract all text from a PDF.
    """

    text = ""

    with fitz.open(file_path) as pdf:

        for page in pdf:
            text += page.get_text()

    return text

###Create Chunk_id
def create_chunk_ids(
    file_hash: str,
    total_chunks: int
) -> List[str]:
    """
    Generate unique IDs for every chunk.
    """

    return [
        f"{file_hash}_{index}"
        for index in range(total_chunks)
    ]

#Create Metadata
def create_metadata(
    file_name: str,
    file_hash: str,
    total_chunks: int
):
    """
    Create metadata for every chunk.
    """

    metadata = []

    for index in range(total_chunks):

        metadata.append(
            {
                "file_name": file_name,
                "file_hash": file_hash,
                "chunk_index": index
            }
        )

    return metadata

vector_service = VectorService()

async def process_pdf(file: UploadFile):

    #read file
    file_bytes = await file.read()

    #Generate hash_code
    file_hash = generate_hash_code(file_byte=file_bytes)

    #Check duplicate
    if vector_service.document_exist(file_hash=file_hash):
        return {
            "success": False,
            "message": "This is already stored in pdf",
            "file_hash": file_hash
        }

    #save pdf_file
    file_path = save_pdf(
        file_name=file.filename,
        file_bytes=file_bytes
        )

    #extract text
    ext_txt = extract_text(file_path=file_path)

    #chunking
    chunks = chunking(ext_txt)

    #embeddings
    embeddings = embedding_documents(chunks) 
                  
    #generate chunks_id
    chunks_ids = create_chunk_ids(file_hash=file_hash,
                                  total_chunks=len(chunks))

    #generate metadata
    metadatas = create_metadata(
        file_name=file.filename, 
        file_hash=file_hash, 
        total_chunks=len(chunks)
        )

    #add in vector database
    vector_service.add_vectors(
        embeddings=embeddings,
        ids=chunks_ids,
        metadatas=metadatas,
        documents=chunks
    )

    return {
        "success":True,
        "message": "PDF uploaded successfully with their indexed.",
        "file_name": file.filename,
        "file_hash": file_hash,
        "chunks": len(chunks)
    }