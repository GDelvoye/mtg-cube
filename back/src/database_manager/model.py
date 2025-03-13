from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class CardPool(Base):
    __tablename__ = "cards_pool"

    index: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    lang: Mapped[str] = mapped_column(String(30))
    cmc: Mapped[Optional[int]]
    type_line: Mapped[str] = mapped_column(String)
    power: Mapped[Optional[int]]
    toughness: Mapped[Optional[int]]
    prices: Mapped[Optional[float]]
    set: Mapped[str]
    oracle_text: Mapped[str]

    def __repr__(self) -> str:
        return f"Card(id={self.index!r}, name={self.name!r})"


# from sqlalchemy import create_engine

# engine = create_engine("sqlite://", echo=True)

# from sqlalchemy.orm import Session

# with Session(engine) as session:
#     black_lotus = Card(
#         name="Black Lotus",
#         type_line="Artifact",
#     )
#     rhox = Card(name="Rhox", type_line="Creature: beast", power=5)
#     session.add_all([black_lotus, rhox])
#     session.commit()
