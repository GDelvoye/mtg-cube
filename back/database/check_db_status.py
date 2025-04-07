from sqlalchemy import inspect


from database.connection import engine, SessionLocal
from database.models import Card


def check_db_status():
    print("🔗 Connected to DB:", engine.url)

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("📦 Tables in DB:", tables)

    if "cards" in tables:
        with SessionLocal() as session:
            count = session.query(Card).count()
            print(f"🃏 Number of rows in 'cards': {count}")
        return tables, count
    else:
        print("⚠️ Table 'cards' does not exist.")
        return tables, None


if __name__ == "__main__":
    check_db_status()
