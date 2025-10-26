 
# RAG System API

This project implements a **Retrieval-Augmented Generation (RAG)** system using FastAPI, where users can upload documents, create embeddings, and ask questions to generate answers based on the provided context.

## Project Overview

The RAG system uses the following components:
- **Document Loader**: To load and process documents.
- **Vector Store**: To store and retrieve document embeddings using similarity search.
- **Mistral**: A language model API used to generate answers based on the retrieved context.

## Features

- **Upload Files**: Upload documents to be processed and embedded into the vector store.
- **Create Embeddings**: Generate embeddings for the uploaded documents.
- **Ask Questions**: Retrieve context from the documents and generate answers based on a user query.

## Prerequisites

- Python 3.13.3 (or compatible version)
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up your environment variables (e.g., `MISTRAL_API_KEY`, `DATA_PATH`) in a `.env` file or directly in your environment.

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation at:

    ```
    http://127.0.0.1:8000/docs
    ```

3. **Upload Files**: Use the `/upload` endpoint to upload documents that will be processed by the RAG system.

4. **Create Embeddings**: Use the `/embed` endpoint to create embeddings for the uploaded documents.

5. **Ask Questions**: Use the `/ask` endpoint to ask questions based on the content of the uploaded documents.

## Example Requests

### 1. Upload Files

- **Endpoint**: `/upload`
- **Method**: `POST`
- **Files**: Multiple files (e.g., `.txt`, `.pdf`)

### 2. Embed Documents

- **Endpoint**: `/embed`
- **Method**: `POST`
- **Response**: `{"message": "Embeddings created successfully"}`

### 3. Ask Questions

- **Endpoint**: `/ask`
- **Method**: `POST`
- **Body**: `query=<your_query>`
- **Response**: The generated answer based on the context of the uploaded documents.
