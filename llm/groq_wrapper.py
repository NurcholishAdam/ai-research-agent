from langchain_groq import ChatGroq
from config import GROQ_API_KEY

def load_groq_llm():
    return ChatGroq(
        model="llama-3-8b-instruct",
        temperature=0.3,
        groq_api_key=GROQ_API_KEY
    )
