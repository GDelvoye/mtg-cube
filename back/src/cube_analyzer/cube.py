from typing import Any
import pandas as pd

from src.database_manager.data_cleaner import format_oracle_text, remove_doublon


def color_proportion(pool_cards: pd.DataFrame) -> dict[str, float]:
    dict_color = {}
    size = pool_cards.shape[0]
    if size == 0:
        return {}

    def is_color_in_list(liste: list, color: str) -> int:
        if liste == []:
            if color == "N":
                return 1
            else:
                return 0
        if color in liste:
            return 1
        return 0

    for color in ["W", "G", "R", "B", "U", "N"]:
        nb_i = (
            pool_cards["colors"].dropna().apply(is_color_in_list, args=(color))
        ).sum()
        dict_color[f"{color}"] = nb_i / size
    return dict_color


def get_dict_cardinal_rarity(card_pool: pd.DataFrame) -> dict[str, int]:
    dict_rarity = {}
    for rarity in ["common", "uncommon", "rare", "mythic"]:
        s = (card_pool["rarity"] == rarity).sum()
        dict_rarity[rarity] = int(s)
    return dict_rarity


def esperance_to_find_keyword_by_booster(
    dict_cardinal_keyword_by_rarity: dict[str, int],
    dict_cardinal_rarity_pool_card: dict[str, int],
) -> float:
    """10*(#keywoard comm) / (#common) + ..."""
    dict_rarity_by_booster = {
        "common": 10,
        "uncommon": 3,
        "rare": 7 / 8,
        "mythic": 1 / 8,
    }
    esperance = 0.0
    for rarity in dict_rarity_by_booster.keys():
        if dict_cardinal_rarity_pool_card[rarity] > 0:
            denom = dict_cardinal_rarity_pool_card[rarity]
        else:
            denom = 1
        esperance += (
            dict_rarity_by_booster[rarity]
            * dict_cardinal_keyword_by_rarity[rarity]
            / denom
        )
    return esperance


class Cube:
    def __init__(self, pool: pd.DataFrame):
        self.pool = pool

    @property
    def size(self) -> int:
        return self.pool.shape[0]

    @property
    def names(self) -> list[str]:
        return list(self.pool["name"])

    @property
    def type_proportion(self) -> dict[str, float]:
        dict_type: dict[str, float] = {}
        if self.size == 0:
            return dict_type
        for typ in [
            "Creature",
            "Instant",
            "Sorcery",
            "Land",
            "Artifact",
            "Enchantment",
            "Planeswalker",
        ]:
            s = self.pool["type_line"].str.contains(typ).sum()
            dict_type[typ] = s / self.size
        return dict_type

    @property
    def rarity_cardinal(self) -> dict[str, int]:
        return get_dict_cardinal_rarity(self.pool)

    @property
    def color_wheel_cardinal(self) -> dict[str, int]:
        """
        Return a dict of the cardinal of the 'color wheel'.
        i.e. the number of uncolored, mono-color, bi-color...
        """
        dict_color = {}

        def len_list(my_list: list) -> int:
            return len(my_list)

        for i in range(6):
            nb_i = (self.pool["colors"].dropna().apply(len_list) == i).sum()
            dict_color[f"{i} colors"] = int(nb_i)
        return dict_color

    @property
    def color_proportion(self) -> dict[str, float]:
        return color_proportion(self.pool)

    def get_pool_filtered(self, text: str) -> pd.DataFrame:
        df_format_text = format_oracle_text(self.pool)
        filtered_pool = df_format_text[
            self.pool["oracle_text"].str.contains(f"(?i){text}", na=False)
        ]
        return remove_doublon(filtered_pool)

    def get_pool_filtered_regex(self, regex: str) -> pd.DataFrame:
        df_format_text = format_oracle_text(self.pool)
        filtered_pool = df_format_text[
            self.pool["oracle_text"].str.contains(regex, case=False, na=False)
        ]
        return remove_doublon(filtered_pool)

    def esperance_to_find_keyword_by_booster(
        self, keyword: str, in_cube: bool = False
    ) -> float:
        pool_with_keyword = self.get_pool_filtered(keyword)
        if in_cube:
            return 15 * pool_with_keyword.shape[0] / self.size
        return esperance_to_find_keyword_by_booster(
            dict_cardinal_keyword_by_rarity=get_dict_cardinal_rarity(
                self.get_pool_filtered(keyword)
            ),
            dict_cardinal_rarity_pool_card=self.rarity_cardinal,
        )

    def esperance_to_find_type_by_booster(
        self, official_booster: bool = True
    ) -> dict[str, float]:
        d = {}
        for type_name in [
            "Creature",
            "Instant",
            "Sorcery",
            "Land",
            "Artifact",
            "Enchantment",
            "Planeswalker",
        ]:
            pool_with_keyword = self.pool[
                self.pool["type_line"].str.contains(type_name)
            ]
            if not official_booster:
                esperance = 15 * pool_with_keyword.shape[0] / self.size
            else:
                esperance = esperance_to_find_keyword_by_booster(
                    dict_cardinal_keyword_by_rarity=get_dict_cardinal_rarity(
                        pool_with_keyword
                    ),
                    dict_cardinal_rarity_pool_card=self.rarity_cardinal,
                )
            d[type_name] = round(esperance, 2)
        return d

    def statistic_summarize(self) -> dict[str, Any]:
        """Return a dict containing a summary of a Cube."""
        return {
            "rarity_cardinal": self.rarity_cardinal,
            "type_proportion": self.type_proportion,
            "color_wheel_cardinal": self.color_wheel_cardinal,
            "color_proportion": self.color_proportion,
            "esperance_type_booster": self.esperance_to_find_type_by_booster(),
        }
