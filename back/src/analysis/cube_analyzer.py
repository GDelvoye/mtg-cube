from typing import Any
import pandas as pd
from enum import Enum

from src.preprocessing.cleaner import drop_duplicate_card_names

NB_CARDS_PER_BOOSTER = 15


class Color(Enum):
    """Enum class of 5 Magic's colors and non-colored."""

    WHITE = "W"
    BLUE = "U"
    BLACK = "B"
    RED = "R"
    GREEN = "G"
    NONE = "N"


class Rarity(Enum):
    """Enum class of all rarity in Magic."""

    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    MYTHIC = "mythic"


class CardType(Enum):
    """All card type."""

    CREATURE = "Creature"
    INSTANT = "Instant"
    SORCERY = "Sorcery"
    LAND = "Land"
    ARTIFACT = "Artifact"
    ENCHANTMENT = "Enchantment"
    PLANESWALKER = "Planeswalker"


def get_color_proportions(cards_deck: pd.DataFrame) -> dict[str, float]:
    """
    Returns the proportions of each color in the given deck of cards.

    Parameters:
        cards_deck: A pandas DataFrame containing a 'colors' column with color data.

    Returns:
        A dictionary mapping each color (from Color Enum) to its proportion in the deck.
    """

    dict_color = {}
    size = cards_deck.shape[0]
    if size == 0:
        return {}

    def is_color_in_list(my_list: list, color: Color) -> int:
        if my_list == []:
            return 1 if color == Color.NONE else 0
        return 1 if color.value in my_list else 0

    for color in Color:
        nb_i = (
            cards_deck["colors"].dropna().apply(is_color_in_list, args=(color,))
        ).sum()
        dict_color[color.value] = float(nb_i / size)
    return dict_color


def get_rarity_counts(cards_deck: pd.DataFrame) -> dict[str, int]:
    dict_rarity_counts = {}
    for rarity in Rarity:
        s = (cards_deck["rarity"] == rarity.value).sum()
        dict_rarity_counts[rarity.value] = int(s)
    return dict_rarity_counts


def compute_expected_value_of_keyword_per_booster(
    dict_keyword_rarity_counts: dict[str, int],
    dict_whole_deck_rarity_counts: dict[str, int],
) -> float:
    """
    Compute the expected value of given keyword occurrences in a single booster.

    10*(nb_of_common_keyword) / (total_nb_of_common) + unco + rare + mythic.

    Parameters:
        dict_keyword_rarity_counts: dict mapping each rarity to the number of cards
            that contain the keyword.
        dict_whole_deck_rarity_counts: dict mapping each rarity to the total number of cards
            in the card pool for that rarity.

    Returns:
        A float
    """

    dict_rarity_distribution_by_booster = {
        Rarity.COMMON.value: 10,
        Rarity.UNCOMMON.value: 3,
        Rarity.RARE.value: 7 / 8,
        Rarity.MYTHIC.value: 1 / 8,
    }
    expected_value = 0.0
    for rarity in dict_rarity_distribution_by_booster.keys():
        if dict_whole_deck_rarity_counts[rarity] > 0:
            denom = dict_whole_deck_rarity_counts[rarity]
        else:
            denom = 1
        expected_value += (
            dict_rarity_distribution_by_booster[rarity]
            * dict_keyword_rarity_counts[rarity]
            / denom
        )
    return expected_value


class CubeAnalyzer:
    """Perform all statistics analysis & regex search."""

    def __init__(self, cards_deck: pd.DataFrame):
        self.cards_deck = cards_deck

    @property
    def size(self) -> int:
        """Return number of cards."""
        return self.cards_deck.shape[0]

    @property
    def names(self) -> list[str]:
        return list(self.cards_deck["name"])

    @property
    def type_proportion(self) -> dict[str, float]:
        dict_type: dict[str, float] = {}
        if self.size == 0:
            return dict_type
        for card_type in CardType:
            s = self.cards_deck["type_line"].str.contains(card_type.value).sum()
            dict_type[card_type.value] = float(s / self.size)
        return dict_type

    @property
    def rarity_counts(self) -> dict[str, int]:
        return get_rarity_counts(self.cards_deck)

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
            nb_i = (self.cards_deck["colors"].dropna().apply(len_list) == i).sum()
            dict_color[f"{i} colors"] = int(nb_i)
        return dict_color

    @property
    def color_proportion(self) -> dict[str, float]:
        return get_color_proportions(self.cards_deck)

    def get_pool_filtered(self, text: str) -> pd.DataFrame:
        df_cards_deck = self.cards_deck
        df_filtered_by_text = df_cards_deck[
            self.cards_deck["oracle_text"].str.contains(f"(?i){text}", na=False)
        ]
        return drop_duplicate_card_names(df_filtered_by_text)

    def get_pool_filtered_regex(
        self, regex: str
    ) -> pd.DataFrame:  # TODO delete if not used.
        df_format_text = self.cards_deck
        filtered_pool = df_format_text[
            self.cards_deck["oracle_text"].str.contains(regex, case=False, na=False)
        ]
        return drop_duplicate_card_names(filtered_pool)

    def get_expected_value_of_keyword_per_booster(
        self,
        keyword: str,
        official_booster: bool = True,
    ) -> float:
        df_filtered_by_keyword = self.get_pool_filtered(keyword)
        if official_booster:
            return compute_expected_value_of_keyword_per_booster(
                dict_keyword_rarity_counts=get_rarity_counts(
                    self.get_pool_filtered(keyword)
                ),
                dict_whole_deck_rarity_counts=self.rarity_counts,
            )
        return NB_CARDS_PER_BOOSTER * df_filtered_by_keyword.shape[0] / self.size

    def get_expected_value_of_all_cards_type_per_booster(
        self, official_booster: bool = True
    ) -> dict[str, float]:
        dict_result = {}
        for card_type in CardType:
            df_filtered_by_type = self.cards_deck[
                self.cards_deck["type_line"].str.contains(card_type.value)
            ]
            if official_booster:
                expected_value = compute_expected_value_of_keyword_per_booster(
                    dict_keyword_rarity_counts=get_rarity_counts(df_filtered_by_type),
                    dict_whole_deck_rarity_counts=self.rarity_counts,
                )
            else:
                expected_value = (
                    NB_CARDS_PER_BOOSTER * df_filtered_by_type.shape[0] / self.size
                )
            dict_result[card_type.value] = round(expected_value, 2)
        return dict_result

    @property
    def cmc_curve(self) -> dict[int, int]:
        """Return dict of key cmc, value cardinal in Cube of key's CMC."""
        dict_cmc = {}
        for i in range(0, 10):
            dict_cmc[i] = int((self.cards_deck["cmc"] == i).sum())
        return dict_cmc

    def statistic_summarize(self) -> dict[str, Any]:
        """Return a dict containing a summary of a Cube."""
        return {
            "rarity_cardinal": self.rarity_counts,
            "type_proportion": self.type_proportion,
            "color_wheel_cardinal": self.color_wheel_cardinal,
            "color_proportion": self.color_proportion,
            "esperance_type_booster": self.get_expected_value_of_all_cards_type_per_booster(),
            "cmc_dict": self.cmc_curve,
        }
