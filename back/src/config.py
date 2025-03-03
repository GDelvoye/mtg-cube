from pathlib import Path


BACK_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACK_DIR.parent / "data"
SQL_DIR = BACK_DIR.parent / "sql_database"
TEST_DIR = BACK_DIR / "tests"

SQL_DB_PATH = SQL_DIR / "cards.db"
TEST_SQL_DB_PATH = TEST_DIR / "data/test.db"
