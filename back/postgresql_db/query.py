from sqlalchemy.orm import Session
from postgresql_db.database import engine, Card, SessionLocal
import pandas as pd


def query_set(set_name: str, db_session: Session):
    exists = db_session.query(Card).filter_by(set=set_name)
    df = pd.read_sql(exists.statement, engine)
    return df


def get_df(set_name: str) -> pd.DataFrame:
    session = SessionLocal()
    df = query_set(set_name, session)
    session.close()
    return df


if __name__ == "__main__":
    set_name = "mrd"
    session = SessionLocal()
    df = query_set(set_name, session)
    session.close()
    print(df)
