from langchain_huggingface import HuggingFaceEmbeddings

def embed_txt(text: str):

    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    embeddings = HuggingFaceEmbeddings(model_name = model_name)

    return embeddings.embed_query(text)
