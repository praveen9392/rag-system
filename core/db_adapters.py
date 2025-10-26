# core/db_adapters.py
from abc import ABC, abstractmethod

class BaseDBAdapter(ABC):
    """Abstract DB adapter."""

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def query(self, query):
        pass

# Example SQLite adapter (can extend later)
import sqlite3
from config import DATA_PATH

class SQLiteAdapter(BaseDBAdapter):
    def __init__(self, db_path="rag.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)
        self.conn.commit()

    def save(self, content: str):
        self.cursor.execute("INSERT INTO documents (content) VALUES (?)", (content,))
        self.conn.commit()

    def query(self, query: str):
        self.cursor.execute("SELECT content FROM documents WHERE content LIKE ?", (f"%{query}%",))
        return self.cursor.fetchall()
