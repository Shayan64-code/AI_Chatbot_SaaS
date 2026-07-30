from langchain_huggingface import HuggingFaceEmbeddings
from Config import embedding_model

embeddings = HuggingFaceEmbeddings(model_name = embedding_model)

#for embedding single chunk
def embedding_txt(chunks: str):

    return embeddings.embed_query(chunks)

#for embedding multiple chunks
def embedding_documents(chunks: list[str]):

    return embeddings.embed_documents(chunks)