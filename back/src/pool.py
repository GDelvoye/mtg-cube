import pandas as pd

from back.src.filter import format_oracle_text, remove_doublon


def color_proportion(pool_cards: pd.DataFrame) -> dict[str, int]:
    dict_color = {}
    size = pool_cards.shape[0]

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
        dict_rarity[rarity] = s
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
    esperance = 0
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


class CardPool:
    def __init__(self, pool: pd.DataFrame):
        self.pool = pool

    @property
    def size(self) -> int:
        return self.pool.shape[0]

    @property
    def type_proportion(self) -> dict[str, float]:
        dict_type = {}
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
    def nb_color_proportion(self) -> dict[str, int]:
        dict_color = {}

        def len_list(liste: list) -> int:
            return len(liste)

        for i in range(6):
            nb_i = (self.pool["colors"].dropna().apply(len_list) == i).sum()
            dict_color[f"{i} couleurs"] = nb_i
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

    def esperance_to_find_keyword_by_booster(self, keyword: str, in_cube: bool = False):
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
        self, in_cube: bool = False
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
            if in_cube:
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
