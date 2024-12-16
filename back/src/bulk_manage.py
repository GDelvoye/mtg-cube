import os

from src.constantes import COLUMNS_TO_DROP

import pandas as pd

from src.price_manager import apply_us_price


def remove_basic_land(pool_cards: pd.DataFrame) -> pd.DataFrame:
    return pool_cards[~pool_cards["type_line"].str.contains("Basic Land", na=False)]


def remove_useless_columns(
    df_bulk: pd.DataFrame, columns_to_drop: list[str] = COLUMNS_TO_DROP
) -> pd.DataFrame:
    return df_bulk.drop(columns=columns_to_drop)


def format_bulk_df(
    df_bulk: pd.DataFrame,
) -> pd.DataFrame:
    """
    Clean the bulk data.

    1. Remove basic land
    2. Convert price dict into US price float
    # 3. Remove all doublons
    4. Remove "A - " cards
    5. Merge card faces texts into oracle_text
    6. Drop useless columns

    return:
        pd.DataFrame
    """
    df_remove_basic = remove_basic_land(df_bulk)
    df_us_price = apply_us_price(df_remove_basic)
    # df = remove_doublon(df)
    return remove_useless_columns(df_us_price)


def create_clean_json_data(
    bulk_json_data_path: str,
    clean_json_data_name: str,
) -> None:
    # with open(bulk_json_data_path, "r") as data_json:
    #     bulk_data = json.load(data_json)
    # data_path = "data/default-cards-20240504210746.json"
    df_bulk = pd.read_json(bulk_json_data_path)
    df_clean = format_bulk_df(df_bulk)
    df_clean.to_json(os.path.join("data", clean_json_data_name))
