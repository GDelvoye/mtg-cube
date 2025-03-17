from typing import Any

from src.cube_analyzer.cube import Cube
import pandas as pd
from src.config import DATA_DIR


def get_set_from_card_pool(set_name: str) -> pd.DataFrame:
    """Read JSON and return DataFrame of all card of same set."""
    json_path = DATA_DIR / "data-clean-en-latest.json"
    df_clean = pd.read_json(json_path)
    df_set = df_clean[df_clean["set"] == set_name]
    return df_set


def generate_visualization_infos_official_set(set_name: str) -> dict[str, Any]:
    """Given a str of an official extension abbrv, trigger a pipeline for getting
    data visualtion dict.

    1. Filter the whole pool against set_name
    2. Build Python object with the previous result
    3. Build a dict with all visu infos.

    Return a dict of key=name of visu and value visu infos."""

    df_set = get_set_from_card_pool(set_name)
    cube = Cube(df_set)

    return cube.statistic_summarize()


if __name__ == "__main__":
    res = generate_visualization_infos_official_set("rav")
    print(res["rarity_cardinal"])
