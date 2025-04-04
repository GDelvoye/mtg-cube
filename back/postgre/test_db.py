from database import SessionLocal, User, Cube, Card

session = SessionLocal()

# User creation
user = User(username="gauthier2")
session.add(user)
session.commit()

print("A")

# User's cube creation
cube = Cube(name="Vintage Cube2", owner=user)
session.add(cube)
session.commit()

print("B")

# Add some cards
card1 = Card(name="Ancestral Recall2")
card2 = Card(name="Wrath of Gods2")

# Association of those cards to Cube
cube.cards.extend([card1, card2])
session.add_all([card1, card2])
session.commit()

print("C")

# Data reading
user_cubes = session.query(Cube).filter_by(owner_id=user.id).all()
for c in user_cubes:
    print(f"Cube:  {c.name}, Cards: {[card.name for card in c.cards]}")


session.close()
