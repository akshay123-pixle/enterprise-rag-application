import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    QDRANT_URL=os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION="enterprise_rag"
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    GROQ_MODEL=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    GROQ_FALLBACK_API_KEY=os.getenv("GROQ_FALLBACK_API_KEY")
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
        # --- LLM GATEWAY (PORTKEY) ---
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    PORTKEY_SAVED_CONFIG_ID = os.getenv("PORTKEY_SAVED_CONFIG_ID")
    GROQ_SLUG =  "rag"     # primary: @rag/llama-3.1-8b-instant
    GROQ_SLUG_2 = "rag"   # fallback: @rag/llama-3.1-8b-instant

settings=Settings()

