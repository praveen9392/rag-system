# core/embeddings.py
from langchain_community.embeddings import HuggingFaceEmbeddings

class EmbeddingProvider:
    """Wrapper for embeddings."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name)

    def get_embeddings(self):
        return self.embeddings
