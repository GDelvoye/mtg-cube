from api.blueprint import bp
import pandas as pd

from src.cardpool import CardPool
from src.filter import filter_by_extension
from src.config import CLEAN_JSON_PATH


@bp.route("/get_test_cube", methods=["GET"])
def get_test_cube() -> dict:
    df_clean = pd.read_json(CLEAN_JSON_PATH)
    df_eld = filter_by_extension(df_clean, ["eld"])
    print(df_eld.shape)

    pool = CardPool(df_eld)
    return pool.to_dict()
