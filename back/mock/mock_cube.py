import pandas as pd

from src.filter import filter_by_extension
from src.config import CLEAN_JSON_PATH
from src.cardpool import CardPool
import pickle


PICKLE_MOCK_CUBE_PATH = "mock/data/mock_test_cube.pkl"


def mock_create_cube() -> CardPool:
    df_clean = pd.read_json(CLEAN_JSON_PATH)
    df_eld = filter_by_extension(df_clean, ["eld"])

    return CardPool(df_eld)


def create_pickle_test_cube() -> None:
    card_pool = mock_create_cube()
    with open(PICKLE_MOCK_CUBE_PATH, "wb") as handle:
        pickle.dump(card_pool, handle)


def mock_load_cube() -> CardPool:
    with open(PICKLE_MOCK_CUBE_PATH, "rb") as handle:
        card_pool = pickle.load(handle)
    return card_pool


if __name__ == "__main__":
    create_pickle_test_cube()
