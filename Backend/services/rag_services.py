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

        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def QA(self, question, embedding_model=embedding_model):
        """
        This method will run the whole process of RAG.
        """
        Embed_Query = embedding_model.encode(question).toList()

        result = self.vector_service.search_vectors(
            query_embeddings=Embed_Query
            )

        #Extract retreive documents
        documents = result["documents"][0]

        #Combine into context
        context = "\n\n".join(documents)

        #Build Prompt
        prompt = f"""
You are a helpful AI assistant.

Answer the question ONLY using the context below.

If the answer is not found in the context,
say "I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}
"""
        response = self.client.chat.completions.create(
            model=embedding_model,
            messages=[
                {
                "role": "user",
                "content": prompt
            }
            ]
        )

        return response.choices[0].message.content.strip()

        ###want to connect it's messages with ai_services then with db