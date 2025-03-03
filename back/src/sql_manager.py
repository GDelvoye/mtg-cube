from src.json_manager import from_bulk_json_to_clean_dataframe
import sqlite3
import json


def create_sql_database_from_json(json_path: str) -> sqlite3.Connection:
    """
    Read json, create and clean dataframe, then convert into SQL.
    Return sqlite2.Connection
    """
    clean_df = from_bulk_json_to_clean_dataframe(json_path)

    for col in clean_df.columns:
        if clean_df[col].apply(lambda x: isinstance(x, list)).any():
            clean_df[col] = clean_df[col].apply(json.dumps)

    conn = sqlite3.connect(":memory:")

    clean_df.to_sql("cards", conn, if_exists="replace", index=False)

    return conn


def save_database_to_file(conn: sqlite3.Connection, db_path: str) -> None:
    disk_conn = sqlite3.connect(db_path)
    with disk_conn:
        conn.backup(disk_conn)
    disk_conn.close()


json_path = "tests/data/cards-test-bulk.json"

# When
result = create_sql_database_from_json(json_path)
save_database_to_file(result, "pipi.db")


def request_query_to_sql_db(
    query: str,
) -> tuple:
    """Open SQL db, make the query, close the DB.
    Return the fetchall tuple."""
    conn = sqlite3.connect("sql_database/cards.db")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return result


# if __name__ == "__main__":
# create_sql_database_from_json(
#     "data/default-cards-latest.json", "sql_database/cards.db"
# )

# query = """
# SELECT *
# FROM cards
# WHERE CAST(power AS INTEGER) > 15
# """

# query = """
# SELECT *
# FROM cards
# WHERE set_name = 'mrd'
# """

# query = "SELECT DISTINCT set FROM cards"

# # table_name = "cards"

# # # Requête SQL pour obtenir les noms de colonnes
# # query = f"PRAGMA table_info({table_name})"
# # LIMIT 2;
# query = """
# SELECT oracle_text
# FROM cards
# WHERE "set" in ("mrd")
# """

# # from query import select_set

# # l = ["mrd", "eld"]
# # query = select_set(l)

# res = request_query_to_sql_db(query)
# print([e[4] for e in res])
