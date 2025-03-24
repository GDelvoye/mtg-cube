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


def get_stat_about_regex(regex: str, set_name: str) -> dict[str, Any]:
    df_set = get_set_from_card_pool(set_name)
    cube = Cube(df_set)
    sub_cube = Cube(cube.get_pool_filtered(regex))
    return {
        "expectancy_regex_by_booster": cube.esperance_to_find_keyword_by_booster(
            regex, in_cube=False
        ),
        "regex_color_proportion": sub_cube.color_proportion,
    }


if __name__ == "__main__":
    # res = generate_visualization_infos_official_set("rav")
    # print(res["rarity_cardinal"])
    res = get_stat_about_regex("affinity|fly", "mrd")
    print(res)
