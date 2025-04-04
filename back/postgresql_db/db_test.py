import psycopg2


conn = psycopg2.connect(
    dbname="mtg_cube",
    user="mtg_user",
    password="password",
    host="localhost",
)

cur = conn.cursor()

# Table creation

cur.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    );
""")

# Card insertion
cur.execute(
    "INSERT INTO cards (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;",
    ("Black Lotus",),
)

# Cards recuperation
cur.execute("SELECT * FROM cards")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()
