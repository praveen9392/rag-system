# logger.py
import logging
from config import LOG_PATH
import os

os.makedirs(LOG_PATH, exist_ok=True)

logger = logging.getLogger("RAG")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(f"{LOG_PATH}/rag.log")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
