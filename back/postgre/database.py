from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from typing import List
from dataclasses import dataclass


DATABASE_URL = "postgresql://mtg_user:password@localhost/mtg_cube"
engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


cube_card_association = Table(
    "cube_card_association",
    Base.metadata,
    Column("cube_id", Integer, ForeignKey("cubes.id"), primary_key=True),
    Column("card.id", Integer, ForeignKey("cards.id"), primary_key=True),
)


@dataclass
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    cubes: Mapped[List["Cube"]] = relationship("Cube", back_populates="owner")


@dataclass
class Cube(Base):
    __tablename__ = "cubes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    owner: Mapped["User"] = relationship("User", back_populates="cubes")
    cards: Mapped[List["Card"]] = relationship(
        "Card", secondary=cube_card_association, back_populates="cubes"
    )


@dataclass
class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    cubes: Mapped[List["Cube"]] = relationship(
        "Cube", secondary=cube_card_association, back_populates="cards"
    )


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
