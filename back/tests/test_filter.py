import pandas as pd
from src.filter import format_bulk_df


def test_format_bulk_df():
    # Given
    df_bulk = pd.read_json("tests/data/cards-test-bulk.json")
    # When
    result = format_bulk_df(df_bulk)
    # Then
    assert result.shape[0] == 18
    assert result.shape[1] == 16
    assert list(result["name"]) == [
        "Fury Sliver",
        "Kor Outfitter",
        "Spirit",
        "Siren Lookout",
        "Web",
        "Surge of Brilliance",
        "Obyra's Attendants // Desperate Parry",
        "Venerable Knight",
        "Wildcall",
        "Mystic Skyfish",
        "Battlewing Mystic",
        "Birds of Paradise",
        "Bronze Horse",
        "Wall of Vipers",
        "Admiral Beckett Brass",
        "Mulch",
        "Whiptongue Hydra",
        "Wall of Roots",
    ]
