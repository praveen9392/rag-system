# core/loaders.py
import os
from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import DATA_PATH

class DocumentLoader:
    """Loads and splits documents into chunks."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_documents(self) -> List[Document]:
        docs = []
        for filename in os.listdir(DATA_PATH):
            path = os.path.join(DATA_PATH, filename)
            if filename.endswith(".txt"):
                loader = TextLoader(path)
            elif filename.endswith(".pdf"):
                loader = PyPDFLoader(path)
            else:
                continue
            docs.extend(loader.load())
        return docs

    def split_documents(self, docs: List[Document]) -> List[Document]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        return splitter.split_documents(docs)
