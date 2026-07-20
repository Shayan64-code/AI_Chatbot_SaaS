from langchain_huggingface import HuggingFaceEmbeddings
from Config import embedding_model

def embed_txt(text: str, model_name = embedding_model):

    embeddings = HuggingFaceEmbeddings(model_name = model_name)

    return embeddings.embed_query(text)
