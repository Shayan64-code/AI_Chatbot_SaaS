import os
from services.vector_services import VectorService

from openai import OpenAI
from Config import embedding_model

class RAGService:
    """
    This class run the process of Retrieval Augmented Generation(RAG).
    """
    def __init__(self):
        self.vector_service = VectorService()

        self.client = os.getenv("OPENAI_API_KEY")

    def QA(self, Question, embedding_model=embedding_model):
        """
        This method will run the whole process of RAG.
        """
        Embed_Query = embedding_model.encode(Question).toList()

        result = self.vector_service.search_vectors(
            query_embeddings=Embed_Query
            )

        self.client
        

