from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()


database_url = os.environ["DATABASE_URL"]

if not database_url:
    raise ValueError("DATABASE_URL env variable not found.")


engine = create_engine(database_url, echo=False)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
