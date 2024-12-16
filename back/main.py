# from src.cardpool import CardPool

import os
import pandas as pd
from src.filter import filter_by_extension
from src.config import CLEAN_JSON_PATH, DATA_PATH
from src.bulk_manage import create_clean_json_data
from src.cardpool import CardPool


if not os.path.exists(CLEAN_JSON_PATH):
    json_path = os.path.join(DATA_PATH, "default-cards-20241209100804.json")
    create_clean_json_data(json_path, CLEAN_JSON_PATH)

df_clean = pd.read_json(CLEAN_JSON_PATH)
df_eld = filter_by_extension(df_clean, ["eld"])
print(df_eld.shape)

pool = CardPool(df_eld)
print("type card", pool.type_cardinal)
print("rare card", pool.rarity_cardinal)
print("color card", pool.nb_color_proportion)
print("color 2", pool.color_proportion)

# word_wanted = "discard"


# with open(json_path, "r") as data_json:
#     data = json.load(data_json)
# print(data)

# df_bulk = pd.read_json(json_path)
# print(df_bulk)
# df_clean = format_bulk_df(df_bulk)
# df_clean.to_json("data/data_clean.json")

# pool = CardPool
