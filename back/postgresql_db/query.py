from sqlalchemy.orm import Session
from database.models import Card
from database.connection import SessionLocal
from database.session import get_db
import pandas as pd


def query_set(set_name: str, db_session: Session):
    exists = db_session.query(Card).filter_by(set=set_name)
    print("RAW SQL: ", exists.statement)
    df = pd.read_sql(exists.statement, db_session.bind)
    return df


def get_df(set_name: str) -> pd.DataFrame:
    for db in get_db():
        print("Connected to DB:", db.bind.url)

        df = query_set(set_name, db)
        print("DFFFF", df)
        return df


if __name__ == "__main__":
    set_name = "mrd"
    session = SessionLocal()
    df = query_set(set_name, session)
    session.close()
    print(df)
