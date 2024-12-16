from typing import Optional
import json
import pandas as pd

from src.bulk_manage import format_bulk_df, remove_useless_columns


def remove_doublon(pool_cards: pd.DataFrame) -> pd.DataFrame:
    """Keep lower price."""
    price_sorted = pool_cards.sort_values(by=["prices"])
    return price_sorted.drop_duplicates(subset=["name"], keep="first")


def merge_two_sided_card_text_into_text_cell(
    text_cell: Optional[str],
    two_sided_text_cell: Optional[list[dict[str, str]]],
) -> str:
    if text_cell is not None:
        return text_cell
    if two_sided_text_cell is not None:
        try:
            merged_text = ""
            for dict_sided in two_sided_text_cell:
                merged_text += dict_sided["type_line"] + ": "
                merged_text += dict_sided["oracle_text"] + "\n"
            return merged_text[:-3]
        except:
            # print(two_sided_text_cell)
            print("2 sided text fail")
            return None
    return None


def format_oracle_text(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["oracle_text"] = df.apply(
        lambda x: merge_two_sided_card_text_into_text_cell(
            x["oracle_text"], x["card_faces"]
        ),
        axis=1,
    )
    return df_new


def filter_by_extension(
    df_clean: pd.DataFrame, extension_list: list[str]
) -> pd.DataFrame:
    """Return dataframe containing only cards of extension_list."""
    df = format_oracle_text(df_clean)
    df_single = remove_doublon(df[df["set"].isin(extension_list)])
    return remove_useless_columns(df_single, ["card_faces"])


if __name__ == "__main__":
    data_path = "data/default-cards-20240501090530.json"
    with open(data_path, "r") as data_json:
        data = json.load(data_json)
    data_path = "data/default-cards-20240504210746.json"
    df_bulk = pd.read_json(data_path)
    df_clean = format_bulk_df(df_bulk)
    df_clean.to_json("data/data_clean.json")
