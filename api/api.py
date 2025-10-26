# api/api.py
from fastapi import FastAPI, UploadFile, Form
import os, shutil
from pipeline.pipeline import RAGPipeline
from config import DATA_PATH
from logger import logger

app = FastAPI(title="RAG System API")
pipeline = RAGPipeline()

@app.post("/upload")
async def upload_file(file: UploadFile):
    os.makedirs(DATA_PATH, exist_ok=True)
    file_path = os.path.join(DATA_PATH, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info(f"File uploaded: {file.filename}")
    return {"message": f" File '{file.filename}' uploaded successfully"}

@app.post("/embed")
async def embed_documents():
    pipeline.create_vector_store()
    return {"message": " Embeddings created successfully"}

@app.post("/ask")
async def ask_question(query: str = Form(...)):
    answer = pipeline.generate_answer(query)
    return {"query": query, "answer": answer}
