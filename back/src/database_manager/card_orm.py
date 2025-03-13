from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Text, Float, Integer

Base = declarative_base()


class Cards(Base):
    __tablename__ = "cards"

    index = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    lang = Column(Text, nullable=False)
    mana_cost = Column(Text)
    cmc = Column(Float)
    type_line = Column(Text)
    oracle_text = Column(Text)
    power = Column(Text)
    toughness = Column(Text)
    colors = Column(Text)
    color_identity = Column(Text)
    keywords = Column(Text)
    set = Column(Text)
    set_name = Column(Text)
    rarity = Column(Text)
    prices = Column(Float)
    card_faces = Column(Text)
