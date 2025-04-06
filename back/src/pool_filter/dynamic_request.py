from typing import Any
from sqlalchemy import (
    create_engine,
    Table,
    Integer,
    MetaData,
    select,
    Select,
    Float,
    or_,
    BinaryExpression,
    Column,
    and_,
    ColumnElement,
)
from sqlalchemy.orm import sessionmaker, Session

from postgresql_db.database import Card

SQL_DB_PATH = "to_find"  #  SQL_DIR / "pipicaca.db"  # "latest.db"  # "cards.db"


def logical_operator_to_apply(
    conditions: list[BinaryExpression[bool]],
    logical_operator: str,
) -> ColumnElement[bool]:
    """Apply AND, OR or NOT operator to conditions."""
    if logical_operator == "and":
        return and_(*conditions)
    elif logical_operator == "or":
        return or_(*conditions)
    not_conditions = [~element for element in conditions]
    return and_(*not_conditions)


def overload_query_with_logical_field(
    key_filter_name: str,
    filters: dict[str, Any],
    query: Select,
    cards_column: Column,
) -> Select:
    if key_filter_name in filters and filters[key_filter_name]:
        conditions = [
            cards_column.ilike(
                f"%{ctype}%"
            )  # Vérifie si le type apparaît dans la chaîne
            for ctype in filters[key_filter_name]
        ]
        query = query.where(
            logical_operator_to_apply(
                conditions, filters[key_filter_name + "_operator"]
            )
        )
    return query


def card_type_query(
    filters: dict[str, Any],
    query: Select,
    cards_table: Table,
) -> Select:
    """Use regex to filter card_type."""
    query = overload_query_with_logical_field(
        "card_type", filters, query, cards_table.c.type_line
    )

    return query


def power_query(
    query: Select,
    filters: dict[str, Any],
    cards_table: Table,
) -> Select:
    """Return a query which has been filtered with min/max power requirements."""
    if "min_or_eq_power" in filters:
        query = query.where(
            cards_table.c.power.cast(Integer) >= filters["min_or_eq_power"]
        )
    if "max_power" in filters:
        query = query.where(cards_table.c.power.cast(Integer) < filters["max_power"])
    return query


def price_query(
    query: Select,
    filters: dict[str, Any],
    cards_table: Table,
) -> Select:
    """Return a query which has been filtered with min/max price requirements."""
    if "min_or_eq_price" in filters:
        query = query.where(
            cards_table.c.prices.cast(Float) >= filters["min_or_eq_price"]
        )
    if "max_price" in filters:
        query = query.where(cards_table.c.prices.cast(Float) < filters["max_price"])
    return query


def dynamic_query_builder(
    filters: dict[str, Any],
    query: Select,
    cards_table: Table,
) -> Select:
    """
    Return overloaded query with appropriate filters dict.
    """
    if "set_list" in filters and filters["set_list"]:
        query = query.where(cards_table.c.set.in_(filters["set_list"]))

    query = power_query(query, filters, cards_table)

    if "min_or_eq_toughness" in filters:
        query = query.where(
            cards_table.c.toughness.cast(Integer) >= filters["min_or_eq_toughness"]
        )
    if "max_toughness" in filters:
        query = query.where(
            cards_table.c.toughness.cast(Integer) < filters["max_toughness"]
        )

    query = price_query(query, filters, cards_table)

    query = overload_query_with_logical_field(
        "card_type", filters, query, cards_table.c.type_line
    )

    return query


class DataBaseManager:
    def __init__(self, sql_db_path: str):
        self.sql_db_path = sql_db_path
        self.engine = create_engine(f"sqlite:///{self.sql_db_path}")
        self.session = self.start_session()
        self.metadata = MetaData()
        self.cards = Table("cards", self.metadata, autoload_with=self.engine)

    def start_session(self) -> Session:
        Session = sessionmaker(bind=self.engine)
        return Session()

    def get_result(
        self,
        query: Select,
        query_filter: dict[str, Any],
    ):
        query = select(Card).where(Card.prices > 2000)
        res = self.session.execute(query).fetchall()

        print(len(res))
        for e in res:
            print(type(e))
            print(e._asdict()["Cards"].name)
            print(e._asdict()["Cards"].prices)
            print(e._mapping["Cards"].cmc)


if __name__ == "__main__":
    db_man = DataBaseManager(str(SQL_DB_PATH))  #  , TEST_SQL_DB_PATH)
    query = select(
        db_man.cards.c.name,
        db_man.cards.c.set,
        db_man.cards.c.cmc,
        db_man.cards.c.prices,
        db_man.cards.c.prices,
        db_man.cards.c.type_line,
        db_man.cards.c.power,
        db_man.cards.c.toughness,
    ).where(True)
    query_filter = {
        # "min_or_eq_power": 2,
        # "max_power": 60,
        # "min_or_eq_toughness": 0,
        # "max_toughness": 60,
        # "min_or_eq_price": 0.5,
        # "max_price": 0.5,
        "card_type": ["creature", "human"],
        "card_type_operator": "not",
    }

    db_man.get_result(query, query_filter)
