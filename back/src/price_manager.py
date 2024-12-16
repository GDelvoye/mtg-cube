from typing import Optional
import pandas as pd


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
