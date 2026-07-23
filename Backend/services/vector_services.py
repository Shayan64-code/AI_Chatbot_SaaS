from database.chroma_db import get_collection

class VectorService:

    def __init__(self, Collection_name: str):

        self.collection = get_collection(Collection_name=None)

    def add_vectors(self, embeddings, ids, metadatas, documents):
        """
        Store and Add vectors
        """
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )

        return {
            "status": "success",
            "message": f"{len(ids)}, Stored Successfully"
        }

    def search_vectors(self, query_embeddings, n_result = 5):
        """
        Search Vectors
        """
        results = self.collection.query(
            query_embeddings=[query_embeddings],
            n_result=n_result
        )

        return results

    def document_exist(self, file_hash: str) -> bool:
        """
        Check whether a document with the given hash
        already exists in ChromaDB.
        """
        result = self.collection.get(
            where={"file_hash": file_hash}
        )

        return len(result["ids"]) > 0

    def delete_vectors(self, ids):

        """Delete vectors with ids."""

        self.collection.delete(ids=ids)

        return {
                    "status": "success",
                    "message": f"{len(ids)}, Stored Successfully"
                }

    def get_vector_count(self):
        """
        Returns total vectors stored.
        """

        return self.collection.count()

    def peek_vectors(self, limit=5):
        """
        Returns first few vectors for debugging.
        """

        return self.collection.peek(limit=limit)