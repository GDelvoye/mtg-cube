from typing import Optional
import pandas as pd

from src.constantes import COLUMNS_TO_DROP


def remove_useless_columns(
    df_bulk: pd.DataFrame, columns_to_drop: list[str] = COLUMNS_TO_DROP
) -> pd.DataFrame:
    return df_bulk.drop(columns=columns_to_drop)


def remove_doublon(pool_cards: pd.DataFrame) -> pd.DataFrame:
    """Keep lower price."""
    price_sorted = pool_cards.sort_values(by=["prices"])
    return price_sorted.drop_duplicates(subset=["name"], keep="first")


def remove_basic_land(pool_cards: pd.DataFrame) -> pd.DataFrame:
    return pool_cards[~pool_cards["type_line"].str.contains("Basic Land", na=False)]


def us_price(dict_price: Optional[dict[str, Optional[float]]]) -> Optional[float]:
    if dict_price is None:
        return None
    if "usd" in dict_price.keys():
        if dict_price["usd"] is not None:
            return float(dict_price["usd"])
    elif "eur" in dict_price.keys():
        if dict_price["eur"] is not None:  # isinstance(dict_price["eur"], str):
            return float(dict_price["eur"])
    return None


def apply_us_price(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["prices"] = df["prices"].apply(us_price)
    return df_new


def merge_two_sided_card_text_into_text_cell(
    text_cell: Optional[str],
    two_sided_text_cell: Optional[list[dict[str, str]]],
) -> Optional[str]:
    if text_cell is not None:
        return text_cell
    if two_sided_text_cell is not None:
        try:
            merged_text = ""
            for dict_sided in two_sided_text_cell:
                merged_text += dict_sided["type_line"] + ": "
                merged_text += dict_sided["oracle_text"] + "\n"
            return merged_text[:-3]
        except Exception as ex:
            print(ex)
            print(two_sided_text_cell)
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


def apply_numeric_values(df_bulk: pd.DataFrame) -> pd.DataFrame:
    """Transform str column int int or float."""
    # Liste des valeurs non numériques à supprimer
    invalid_values = {
        "*",
        "*²",
        "?",
        "∞",
        "1+*",
        "2+*",
        "+2",
        "+4",
        "+0",
        "+3",
        "-1",
        "3.5",
        "2.5",
        "1.5",
        "0.5",
        ".5",
        "1.4",
        "1.3",
    }

    for col in ("power", "toughness", "cmc"):
        # Remplacement des valeurs invalides par NaN
        df_bulk[col] = df_bulk[col].replace(invalid_values, None)

        # Conversion en float (coerce pour éviter les erreurs)
        df_bulk[col] = pd.to_numeric(df_bulk[col], errors="coerce").round()

        # Conversion en Int64 (nullable)
        df_bulk[col] = df_bulk[col].astype("Int64")

    for col in ["prices"]:
        # Remplacement des valeurs invalides par NaN
        df_bulk[col] = df_bulk[col].replace(invalid_values, None)

        # Conversion en float (coerce pour éviter les erreurs)
        df_bulk[col] = pd.to_numeric(df_bulk[col], errors="coerce")

    return df_bulk


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
    df_column = remove_useless_columns(df_us_price)

    return apply_numeric_values(df_column)


def filter_by_extension(
    df_clean: pd.DataFrame, extension_list: list[str]
) -> pd.DataFrame:
    """Return dataframe containing only cards of extension_list."""
    df = format_oracle_text(df_clean)
    df_single = remove_doublon(df[df["set"].isin(extension_list)])
    return df_single
    # return remove_useless_columns(df_single, ["card_faces"])


if __name__ == "__main__":
    # data_path = "data/default-cards-en-latest.json"
    # with open(data_path, "r") as data_json:
    #     data = json.load(data_json)
    from src.config import DATA_DIR

    data_path = DATA_DIR / "default-cards-en-latest.json"
    df_bulk = pd.read_json(data_path)
    df_clean = format_bulk_df(df_bulk)
    df_clean.to_json(DATA_DIR / "data-clean-en-latest.json")
