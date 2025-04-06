from pathlib import Path


BACK_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BACK_DIR.parent / "data-full"
JSON_DB = DATA_DIR / "default-cards-en-latest.json"  # Attention
TEST_JSON_DB = DATA_DIR / "simply-cards.json"
