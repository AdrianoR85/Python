import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "../data/myDatabase.db")
cursor = conn.cursor()