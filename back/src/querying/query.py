from sqlalchemy.orm import Session
from sqlalchemy import String, and_, func, cast
from database.models import Card
from sqlalchemy.dialects.postgresql import ARRAY


def build_color_filter(colors_filter: dict):
    colors = colors_filter.get("values", [])
    mode = colors_filter.get("mode", "any")

    if not colors:
        return None

    if mode == "any":
        # colors && ARRAY[...] (au moins une en commun)
        # return Card.colors.op("&&")(colors)
        return func.jsonb_exists_any(Card.colors, cast(colors, ARRAY(String)))

    elif mode == "all_or_more":
        # colors @> ARRAY[...] (contient au moins toutes)
        return Card.colors.contains(colors)

    elif mode == "exact":
        # colors = ARRAY[...]
        return Card.colors == colors

    else:
        raise ValueError(f"Unknown color filter mode: {mode}")


def advanced_card_search(filters: dict, db: Session):
    query = db.query(Card)
    conditions = []

    # Exemple de filtres simples
    if "name" in filters:
        conditions.append(Card.name.ilike(f"%{filters['name']}%"))

    if "lang" in filters:
        conditions.append(Card.lang == filters["lang"])

    if "mana_cost" in filters:
        conditions.append(Card.mana_cost == filters["mana_cost"])

    if "cmc_min" in filters:
        conditions.append(Card.cmc >= filters["cmc_min"])
    if "cmc_max" in filters:
        conditions.append(Card.cmc <= filters["cmc_max"])

    if "type_line" in filters:
        conditions.append(Card.type_line.ilike(f"%{filters['type_line']}%"))

    if "oracle_text" in filters:
        conditions.append(Card.oracle_text.ilike(f"%{filters['oracle_text']}%"))

    # Champs JSON : recherche de couleur
    # if "colors" in filters:
    #     for color in filters["colors"]:
    #         conditions.append(Card.colors.contains([color]))
    if "colors" in filters:
        color_condition = build_color_filter(filters["colors"])
        if color_condition is not None:
            conditions.append(color_condition)

    if "color_identity" in filters:
        for color in filters["color_identity"]:
            conditions.append(Card.color_identity.contains([color]))

    if "keywords" in filters:
        for keyword in filters["keywords"]:
            conditions.append(Card.keywords.contains([keyword]))

    if "set" in filters:
        conditions.append(Card.set == filters["set"])
    if "set_name" in filters:
        conditions.append(Card.set_name == filters["set_name"])
    if "rarity" in filters:
        conditions.append(Card.rarity == filters["rarity"])

    # Filtres numériques
    if "price_min" in filters:
        conditions.append(Card.prices >= filters["price_min"])
    if "price_max" in filters:
        conditions.append(Card.prices <= filters["price_max"])
    if "power_min" in filters:
        conditions.append(Card.power >= filters["power_min"])
    if "power_max" in filters:
        conditions.append(Card.power <= filters["power_max"])
    if "toughness_min" in filters:
        conditions.append(Card.toughness >= filters["toughness_min"])
    if "toughness_max" in filters:
        conditions.append(Card.toughness <= filters["toughness_max"])

    # Appliquer les conditions si présentes
    if conditions:
        query = query.filter(and_(*conditions))

    return query.all()


def search(filters: dict):
    from database.connection import SessionLocal

    with SessionLocal() as db:
        results = advanced_card_search(filters, db)
        # l_result = []

        for card in results:
            # l_result.append([])
            # print(card.name, card.colors)  # , card.power, card.oracle_text)
            pass
        return results


if __name__ == "__main__":
    from database.connection import SessionLocal

    filters = {
        "name": "dragon",
        "colors": {"values": ["R", "W"], "mode": "any"},
        # "price_min": 0.5,
        # "price_max": 10,
        # "power_min": 5,
        # "power_max": 7,
        # "oracle_text": "flying",
    }

    with SessionLocal() as db:
        results = advanced_card_search(filters, db)

        for card in results:
            print(card.name, card.colors)  # , card.power, card.oracle_text)
