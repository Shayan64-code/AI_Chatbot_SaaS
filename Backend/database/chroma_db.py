import chromadb
import os

from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_Path = os.getenv("CHROMA_DB_PATH")
CHROMA_COLLECTION = os.getenv("CHROMA_Collections")

chroma_client = chromadb.PersistentClient(path= CHROMA_DB_Path)

def get_collection(name: str = CHROMA_COLLECTION):

    """
    Returns an existing collection or create new one.
    
    Args: Collection name (str)
    
    Returns: Chroma_db Colections
    
    """

    if name is None:
        name = CHROMA_COLLECTION

    return chroma_client.get_or_create_collection(
        name=name, 
        metadata= {"description": "Stores PDF embeddings"}
        )

def list_collection():
    """
    It will list all collections
    """
    return chroma_client.list_collections

def delete_collection(name: str):
    """
    Delete Collection
    """
    chroma_client.delete_collection(name=name)

def reset_database():
    """
    Delete all collections from Chroma_db
    """
    collections = chroma_client.list_collections

    for collection in collections:
        chroma_client.delete_collection(name=collection.name)

    print("✅ ChromaDB has been reset.")