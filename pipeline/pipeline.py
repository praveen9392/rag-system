# pipeline/pipeline.py
from core.loaders import DocumentLoader
from core.vector_store import FaissVectorStore, VectorStore
from mistralai import Mistral
from config import MISTRAL_API_KEY, LLM_MODEL
from logger import logger


class RAGPipeline:
    """Implements a Retrieval-Augmented Generation (RAG) pipeline."""

    def __init__(self):
        """Initialize the document loader, vector store, and LLM client."""
        self.loader = DocumentLoader()
        self.vector_store = FaissVectorStore()
        self.client = Mistral(api_key=MISTRAL_API_KEY)

    def create_vector_store(self):
        """Load, split, embed, and store documents in the vector database."""
        logger.info("Loading documents...")
        docs = self.loader.load_documents()

        logger.info("Splitting documents...")
        chunks = self.loader.split_documents(docs)

        logger.info("Creating embeddings and vector store...")
        self.vector_store.from_documents(chunks)

        logger.info("Vector store created successfully!")

    def retrieve(self, query: str, k: int = 10):
        """Retrieve the most relevant document chunks for a given query."""
        db = self.vector_store.load()
        docs = db.similarity_search(query, k=k)
        return "\n\n".join([d.page_content for d in docs])

    def generate_answer(self, query: str):
        """Generate an answer to a user query using retrieved context."""
        context = self.retrieve(query)
        prompt = f"""
                    You are a helpful assistant. You will be provided with context below and a question that the user has asked. Your job is to provide an accurate, informative, and relevant answer based on the context. 

                    Context:
                    {context}

                    Question: {query}

                    Answer: 
                    - If the question is asking for specific information (such as facts, names, dates, etc.), provide the most accurate answer based on the context.
                    - If the question asks for a list (such as names, items, or steps), extract and list all relevant items clearly.
                    - If the question asks for a summary or explanation, summarize the key points or concepts from the context.
                    - If the context does not provide enough information to answer the question, explain the limitations of the context and provide the best response possible, clarifying any uncertainties or ambiguities.
                    - If the question involves comparing or analyzing data, do so using the information from the context.

                    Always ensure your response is **direct, clear, and based on the provided context**.
                    """


        response = self.client.chat.complete(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
