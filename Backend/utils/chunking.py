from langchain_text_splitters import RecursiveCharacterTextSplitter
import hashlib

def chunking(text: str, chunk: int = 500, overlap: int = 50):

    splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 100 
    )

    split_docs = splitter.split_text(text)

    return split_docs
