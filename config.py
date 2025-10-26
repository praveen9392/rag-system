# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Mistral API key
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Model and embedding settings
EMBEDDING_MODEL = "mistral-embed"       # placeholder for embedding model
LLM_MODEL = "mistral-small"             # main chat model

# Paths
DATA_PATH = "data"
VECTOR_STORE_PATH = "embeddings/vector_store"
LOG_PATH = "logs"
