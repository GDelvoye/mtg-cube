from json_manager import from_bulk_json_to_clean_dataframe
import sqlite3
import json


def create_sql_database_from_json(json_path: str, sql_database_name: str) -> None:
    """
    Read json, create and clean dataframe, then convert ibnto SQL.
    """
    clean_df = from_bulk_json_to_clean_dataframe(json_path)

    for col in clean_df.columns:
        if clean_df[col].apply(lambda x: isinstance(x, list)).any():
            clean_df[col] = clean_df[col].apply(json.dumps)
    conn = sqlite3.connect(sql_database_name)

    clean_df.to_sql("cards", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_sql_database_from_json(
        "data/default-cards-latest.json", "sql_database/cards.db"
    )
