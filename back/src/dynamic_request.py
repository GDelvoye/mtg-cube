from typing import Any, Optional
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Float,
    MetaData,
    select,
    text,
    Select,
)
from sqlalchemy.orm import sessionmaker, Session
from src.config import SQL_DB_PATH, TEST_SQL_DB_PATH
from dataclasses import dataclass


@dataclass
class QueryFilter:
    set_list: Optional[list[str]] = None
    min_or_eq_power: int = 0
    max_power: int = 99
    min_or_eq_toughness: int = 0
    max_toughness: int = 99

    def build_query(
        self,
        query: Select,
        cards_table: Table,
    ) -> Select:
        """
        Return overloaded query with appropriate filters dict.
        """
        if self.set_list is not None:
            query = query.where(cards_table.c.set.in_(self.set_list))

        query = query.where(
            self.min_or_eq_power <= cards_table.c.power.cast(Integer)  #
        )

        query = query.where(
            self.min_or_eq_toughness <= cards_table.c.toughness.cast(Integer)
            # < self.max_toughness
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
        query_filter: QueryFilter,
    ):
        query = query_filter.build_query(query, self.cards)
        res = self.session.execute(query).fetchall()
        for row in res:
            print(row.name)


if __name__ == "__main__":
    db_man = DataBaseManager(TEST_SQL_DB_PATH)
    query = select(db_man.cards.c.name, db_man.cards.c.set).where(True)
    query_filter = QueryFilter()
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


# def dynamic_query_builder(
#     filters: dict[str, Any],
#     query: Select,
#     cards_table: Table,
# ) -> Select:
#     """
#     Return overloaded query with appropriate filters dict.
#     """
#     if "sets" in filters and filters["sets"]:
#         query = query.where(cards_table.c.set.in_(filters["sets"]))

#     if "min_or_eq_power" in filters:
#         query = query.where(
#             cards_table.c.power.cast(Integer) >= filters["min_or_eq_power"]
#         )
#     if "max_power" in filters:
#         query = query.where(cards_table.c.power.cast(Integer) < filters["max_power"])

#     return query


# results = session.execute(query).fetchall()

# print(len(results))

# for row in results:
#     print(row.name)
