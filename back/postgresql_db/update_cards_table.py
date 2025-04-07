from database.models import Card
from database.connection import SessionLocal
from sqlalchemy.orm import Session
import pandas as pd


def populate_cards_from_dataframe(df: pd.DataFrame, db_session: Session) -> None:
    """
    Insère en base les cartes du DataFrame qui n'existent pas encore (selon `id_full`).
    """

    for _, row in df.iterrows():
        id_full = row["id"]

        # Check if card already in database
        exists = db_session.query(Card).filter_by(id_full=id_full).first()
        if exists:
            continue

        card = Card(
            id_full=row["id"],
            name=row["name"],
            lang=row["lang"],
            mana_cost=row.get("mana_cost"),
            cmc=row.get("cmc"),
            type_line=row.get("type_line"),
            oracle_text=row.get("oracle_text"),
            colors=row.get("colors"),
            color_identity=row.get("color_identity"),
            keywords=row.get("keywords"),
            set=row["set"],
            set_name=row["set_name"],
            rarity=row["rarity"],
            prices=row.get("prices"),
            power=row.get("power"),
            toughness=row.get("toughness"),
        )

        db_session.add(card)

    db_session.commit()


if __name__ == "__main__":
    from src.preprocessing.cleaner import from_bulk_df_to_pre_database
    from src.config import JSON_DB
    import numpy as np

    df_bulk = pd.read_json(JSON_DB)
    df = from_bulk_df_to_pre_database(df_bulk)
    df = df.replace({np.nan: None})
    print(df.head())
    session = SessionLocal()
    populate_cards_from_dataframe(df, session)
    session.close()
