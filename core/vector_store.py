# core/vector_store.py
import os
from langchain_community.vectorstores import FAISS
from core.embeddings import EmbeddingProvider
from config import VECTOR_STORE_PATH

class VectorStore:
    """Base class for vector stores."""

    def save(self, store):
        os.makedirs(os.path.dirname(VECTOR_STORE_PATH), exist_ok=True)
        store.save_local(VECTOR_STORE_PATH)

    def load(self):
        embeddings = EmbeddingProvider().get_embeddings()
        return FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)


class FaissVectorStore(VectorStore):
    """FAISS vector store implementation."""

    def from_documents(self, documents):
        embeddings = EmbeddingProvider().get_embeddings()
        db = FAISS.from_documents(documents, embeddings)
        self.save(db)
        return db
