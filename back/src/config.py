from pathlib import Path


BACK_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACK_DIR.parent / "data"
JSON_DB = DATA_DIR / "default-cards-en-100.json"  # Attention
TEST_JSON_DB = DATA_DIR / "simply-cards.json"

SQL_DIR = BACK_DIR.parent / "sql_database"
TEST_DIR = BACK_DIR / "tests"

SQL_DB_PATH = SQL_DIR / "pipicaca.db"  # "latest.db"  # "cards.db"
TEST_SQL_DB_PATH = TEST_DIR / "data/test.db"
