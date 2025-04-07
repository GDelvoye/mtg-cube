from postgresql_db.database import User, SessionLocal


def create_user(username: str, user_pass: str):
    user = User(username=username)
    user.set_password(user_pass)
    session = SessionLocal()
    session.add(user)
    session.commit()


if __name__ == "__main__":
    create_user("gauthier", "eldars")
