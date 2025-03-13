from sqlalchemy import create_engine, select

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


# with engine.connect() as conn:
#     result = conn.execute(text("select 'hellow world'"))
#     print(result.all())

# # commit as you go (better for demo)
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

# # begin once (to be privilegied)
# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#     )

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     # for row in result:
#     #     print(f"x: {row.x} y:{row.y}")
#     for x, y in result:
#         print(x + y)

from sqlalchemy.orm import Session

# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    pass
    # result = session.execute(stmt, {"y": 6})
    # for x, y in result:
    #     print(x, y)

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

print(user_table.c.keys())
print(user_table.primary_key)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


print(Base.registry)

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email={self.email_address!r})"


Base.metadata.create_all(engine)

from sqlalchemy import insert

stmt = insert(user_table).values(name="speongebob", fullname="bite")

with engine.connect() as conn:
    es = conn.execute(stmt)
    conn.commit()

# some_table = Table("some_table", metadata_obj, autoload_with=engine)

# print(type(some_table))
# print(some_table.columns)

print(select(User))

row = session.execute(select(User)).first()

print(row)
