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
from src.config import TEST_SQL_DB_PATH


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
    # print(filters["card_type"])

    # if "card_type" in filters and filters["card_type"]:
    #     print(type(cards_table.c.type_line))
    #     conditions = [
    #         cards_table.c.type_line.ilike(
    #             f"%{ctype}%"
    #         )  # Vérifie si le type apparaît dans la chaîne
    #         for ctype in filters["card_type"]
    #     ]
    #     query = query.where(
    #         logical_operator_to_apply(conditions, filters["card_type_operator"])
    #     )
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


# @dataclass
# class QueryFilter:
#     set_list: Optional[list[str]] = None
#     min_or_eq_power: int = 0
#     max_power: int = 99
#     min_or_eq_toughness: int = 0
#     max_toughness: int = 99

#     def build_query(
#         self,
#         query: Select,
#         cards_table: Table,
#     ) -> Select:
#         """
#         Return overloaded query with appropriate filters dict.
#         """
#         if self.set_list is not None:
#             query = query.where(cards_table.c.set.in_(self.set_list))

#         query = query.where(
#             self.min_or_eq_power <= cards_table.c.power.cast(Integer)  #
#         )

#         query = query.where(
#             self.min_or_eq_toughness <= cards_table.c.toughness.cast(Integer)
#             # < self.max_toughness
#         )
#         return query


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
        query = dynamic_query_builder(query_filter, query, self.cards)
        res = self.session.execute(query).fetchall()
        i = 0
        for row in res:
            i += 1
            print(
                row.name, row.cmc, row.prices, row.type_line, row.power, row.toughness
            )
        print(f"TOTAL: {i}")


if __name__ == "__main__":
    db_man = DataBaseManager(TEST_SQL_DB_PATH)
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


# def get_cards_table(
#     sql_db_path: str,
# ) -> Table:
#     engine = create_engine(f"sqlite:///{sql_db_path}")

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     metadata = MetaData()
#     return Table("cards", metadata, autoload_with=engine)


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
#     tables = result.fetchall()
#     print("Tables existantes dans la base :", [t[0] for t in tables])


# from sqlalchemy import inspect

# inspector = inspect(engine)
# columns = inspector.get_columns("cards")

# print("Colonnes de la table 'cards' :")
# for col in columns:
#     print(f"- {col['name']} ({col['type']})")


# filters = {
#     "sets": ["eld"],
#     "min_or_eq_power": 5,
#     "max_power": 6,
#     "min_or_eq_toughness": 5,
#     "max_toughness": 6,
#     "min_or_eq_price": 1,
#     "max_price": 2,
# }

# query = select(cards.c.name, cards.c.set).where(True)


# results = session.execute(query).fetchall()

# print(len(results))

# for row in results:
#     print(row.name)
