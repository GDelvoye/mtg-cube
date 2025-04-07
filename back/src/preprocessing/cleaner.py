from typing import Optional
import pandas as pd

from src.preprocessing.constantes import COLUMNS_TO_DROP, COLUMNS_TO_KEEP


def remove_useless_columns(
    df_bulk: pd.DataFrame, columns_to_drop: list[str] = COLUMNS_TO_DROP
) -> pd.DataFrame:
    return df_bulk.drop(columns=columns_to_drop)


def keep_only_relevant_columns(
    df_bulk: pd.DataFrame, columns_to_keep: list[str] = COLUMNS_TO_KEEP
) -> pd.DataFrame:
    return df_bulk[[col for col in columns_to_keep if col in df_bulk.columns]]


def drop_duplicate_card_names(pool_cards: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with duplicate card names removed.

    Keep the lowest price row.
    """
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


def merge_text_of_two_sided_cards(
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
            print("TOTO")
            print(ex)
            print(two_sided_text_cell)
            return None
    return None


def format_oracle_text(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    df_new["oracle_text"] = df.apply(
        lambda x: merge_text_of_two_sided_cards(x["oracle_text"], x["card_faces"]),
        axis=1,
    )
    return df_new


def apply_numeric_values(df_bulk: pd.DataFrame) -> pd.DataFrame:
    """Transform str column int int or float."""
    # Liste des valeurs non numériques à supprimer
    df_bulk = df_bulk.copy()  #  To avoid SettingWithCopyWarning
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


def select_only_expansion_and_core(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["set_type"].isin(["expansion", "core", "commander"])]
    return df


def from_bulk_df_to_pre_database(
    df_bulk: pd.DataFrame,
) -> pd.DataFrame:
    """
    Clean the bulk data, return dataframe to feed the database

    1. Remove basic land
    2. Convert price dict into US price float
    4. Remove "A - " cards ???
    5. Merge card faces texts into oracle_text ?????
    6. Keep only relevant columns
    7. Transform all numeric string into int or float.

    return:
        pd.DataFrame
    """
    # Set NaN to None
    df_bulk = df_bulk.where(pd.notnull(df_bulk), None)
    df_remove_basic = remove_basic_land(df_bulk)
    print("basic removed")
    df_us_price = apply_us_price(df_remove_basic)
    print("us_price_applied")
    # df = remove_doublon(df)
    # df_column = remove_useless_columns(df_us_price)
    df_format_text = format_oracle_text(df_us_price)
    print("text formatted")
    df_column = keep_only_relevant_columns(df_format_text)
    print("good column keeped")
    df_column = select_only_expansion_and_core(df_column)

    return apply_numeric_values(df_column)
