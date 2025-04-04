from postgresql_db.database import SessionLocal, Card, User, Cube


session = SessionLocal()

# Add cards
# new_card = Card(name="Mox Ruby 2")
# session.add(new_card)
# session.commit()


# Read Cards
cards = session.query(Card).all()
for card in cards:
    print(f"CARDS ||| ID: {card.id}, name: {card.name}")

# Read Users
users = session.query(User).all()
for user in users:
    print(
        f"USERS |||| Id: {user.id}, name: {user.username}, cube: {[cube.name for cube in user.cubes]}"
    )

# Read Cubes
cubes = session.query(Cube).all()
for cube in cubes:
    print(
        f"CUBES |||| Id: {cube.id}, name: {cube.name}, owner: {cube.owner.username}, cards: {[card.name for card in cube.cards]}"
    )

session.close()
