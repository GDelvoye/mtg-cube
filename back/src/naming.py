from typing import Any

from src.analysis.cube_analyzer import CubeAnalyzer
import pandas as pd
from src.config import JSON_DB
from postgresql_db.query import get_df


def get_set_from_card_pool(set_name: str) -> pd.DataFrame:
    """Read JSON and return DataFrame of all card of same set."""
    json_path = JSON_DB
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

    # df_set = get_set_from_card_pool(set_name)
    df_set = get_df(set_name)
    cube = CubeAnalyzer(df_set)

    return cube.statistic_summarize()


def get_stat_about_regex(regex: str, set_name: str) -> dict[str, Any]:
    # df_set = get_set_from_card_pool(set_name)
    df_set = get_df(set_name)
    cube = CubeAnalyzer(df_set)
    sub_cube = CubeAnalyzer(cube.get_pool_filtered(regex))
    return {
        "expectancy_by_booster": cube.get_expected_value_of_keyword_per_booster(
            regex, official_booster=True
        ),
        "color_proportion": sub_cube.color_proportion,
    }


if __name__ == "__main__":
    # res = generate_visualization_infos_official_set("rav")
    # print(res["rarity_cardinal"])
    reg = "affinity|fly"
    reg = "sacrifice"
    res = get_stat_about_regex(reg, "mrd")
    print(res)
