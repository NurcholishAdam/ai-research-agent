from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def init_vector_db():
    embedding = OpenAIEmbeddings()
    return Chroma(embedding_function=embedding)

