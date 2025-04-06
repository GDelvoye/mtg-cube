from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    JSON,
    Float,
    String,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from typing import List, Optional
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()


# DATABASE_URL = "postgresql://mtg_user:password@localhost/mtg_cube"
# db_url = os.getenv("DATABASE_URL")
# engine = create_engine(db_url)
DATABASE_URL = "postgresql://postgres:JNvhXBWpVenDSFaOIEOPPlVwmlKSsETU@caboose.proxy.rlwy.net:24041/railway"
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
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    cubes: Mapped[List["Cube"]] = relationship("Cube", back_populates="owner")

    def set_password(self, raw_password: str) -> None:
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password_hash, raw_password)


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
    id_full: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    lang: Mapped[str] = mapped_column(String, nullable=False)
    mana_cost: Mapped[str] = mapped_column(String, nullable=True)
    cmc: Mapped[Optional[str]] = mapped_column(Integer, nullable=True)
    type_line: Mapped[str] = mapped_column(String, nullable=True)
    oracle_text: Mapped[str] = mapped_column(String, nullable=True)

    colors: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=True)
    color_identity: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=False)
    keywords: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=True)
    # produced_mana: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=True)

    # legalities: Mapped[Optional[Dict[str, str]]] = mapped_column(JSON, nullable=False)

    set: Mapped[str] = mapped_column(String, nullable=False)
    set_name: Mapped[str] = mapped_column(String, nullable=False)
    # set_type: Mapped[str] = mapped_column(String, nullable=False)
    rarity: Mapped[str] = mapped_column(String, nullable=False)

    prices: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    power: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    toughness: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    cubes: Mapped[List["Cube"]] = relationship(
        "Cube", secondary=cube_card_association, back_populates="cards"
    )


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
