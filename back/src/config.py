from pathlib import Path


BACK_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACK_DIR.parent / "data"
SQL_DIR = BACK_DIR.parent / "sql_database"

SQL_DB_PATH = SQL_DIR / "cards.db"
