from src.preprocessing.cleaner import (
    merge_text_of_two_sided_cards,
    format_oracle_text,
)
import pandas as pd

dico = [
    {
        "object": "card_face",
        "name": "Obyra's Attendants",
        "mana_cost": "{4}{U}",
        "type_line": "Creature — Faerie Wizard",
        "oracle_text": "Flying",
        "power": "3",
        "toughness": "4",
        "flavor_text": "Obyra's devoted servants shrieked as their sleeping mistress slashed at them, unseeing.",
        "artist": "Andreas Zafiratos",
        "artist_id": "e2f13a9a-57c5-40de-81d4-3b0723899cdf",
        "illustration_id": "d1ea5321-62e2-4894-a79f-03b792daf2c8",
    },
    {
        "object": "card_face",
        "name": "Desperate Parry",
        "mana_cost": "{1}{U}",
        "type_line": "Instant — Adventure",
        "oracle_text": "Target creature gets -4/-0 until end of turn. (Then exile this card. You may cast the creature later from exile.)",
        "artist": "Andreas Zafiratos",
        "artist_id": "e2f13a9a-57c5-40de-81d4-3b0723899cdf",
    },
]


def test_merge_two_sided_card_text_into_text_cell():
    # Given
    text_cell = None
    two_sided_text_cell = [
        {
            "object": "card_face",
            "name": "Obyra's Attendants",
            "mana_cost": "{4}{U}",
            "type_line": "Creature — Faerie Wizard",
            "oracle_text": "Flying",
            "power": "3",
            "toughness": "4",
            "flavor_text": "Obyra's devoted servants shrieked as their sleeping mistress slashed at them, unseeing.",
            "artist": "Andreas Zafiratos",
            "artist_id": "e2f13a9a-57c5-40de-81d4-3b0723899cdf",
            "illustration_id": "d1ea5321-62e2-4894-a79f-03b792daf2c8",
        },
        {
            "object": "card_face",
            "name": "Desperate Parry",
            "mana_cost": "{1}{U}",
            "type_line": "Instant — Adventure",
            "oracle_text": "Target creature gets -4/-0 until end of turn. (Then exile this card. You may cast the creature later from exile.)",
            "artist": "Andreas Zafiratos",
            "artist_id": "e2f13a9a-57c5-40de-81d4-3b0723899cdf",
        },
    ]
    # When
    result = merge_text_of_two_sided_cards(text_cell, two_sided_text_cell)
    # Then
    assert (
        result
        == "Creature — Faerie Wizard: Flying\nInstant — Adventure: Target creature gets -4/-0 until end of turn. (Then exile this card. You may cast the creature later from exile"
    )


def test_format_oracle_text():
    # Given
    df = pd.DataFrame(
        {
            "oracle_text": ["a text", None, None],
            "card_faces": ["an other text", None, dico],
        }
    )
    # When
    result = format_oracle_text(df)
    # Then
    assert result["oracle_text"].values[0] == "a text"
    assert result["oracle_text"].values[1] is None
    assert result["oracle_text"].values[2] is not None
