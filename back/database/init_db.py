from database.connection import Base, engine
import database.models  #  noqa: F401

Base.metadata.create_all(engine)
