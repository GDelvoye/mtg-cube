# from src.cardpool import CardPool

from src.config import SQL_DB_PATH
from src.sql_manager import inspect_database

inspect_database(SQL_DB_PATH)

# word_wanted = "discard"

# json_path = "data/example.json"

# with open(json_path, "r") as data_json:
#     data = json.load(data_json)
# print(data)

# df_bulk = pd.read_json(json_path)
# print(df_bulk)
# df_clean = format_bulk_df(df_bulk)
# df_clean.to_json("data/data_clean.json")

# pool = CardPool
