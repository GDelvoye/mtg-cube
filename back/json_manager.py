import pandas as pd
from src.filter import format_bulk_df


def from_bulk_json_to_clean_dataframe(
    bulk_json_path: str,
) -> pd.DataFrame:
    """Open json bulk file, clean it and return a pandas Dataframe."""
    df_bulk = pd.read_json(bulk_json_path)
    return format_bulk_df(df_bulk)
