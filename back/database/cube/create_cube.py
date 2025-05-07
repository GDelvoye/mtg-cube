from database.exceptions import CubeAlreadyExists, CubeNotFound, UserNotFoundError
from database.models import Card, Cube, User
from sqlalchemy.orm import Session

from database.session import get_db


def get_user(db: Session, username: str) -> User:
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise UserNotFoundError(username)
    return user


def get_cube(db: Session, user_id: int, cube_name: str) -> Cube:
    cube = db.query(Cube).filter_by(name=cube_name, owner_id=user_id).first()
    if not cube:
        raise CubeNotFound(cube_name)
    return cube


def get_card(db: Session, card_full_id: str) -> Card:
    card = db.query(Card).filter_by(id_full=card_full_id).first()
    if not card:
        raise ValueError(f"Card id '{card_full_id}' does not exists.")
    return card


def create_new_cube(db: Session, username: str, cube_name: str) -> None:
    user = get_user(db, username)

    existing_cube = db.query(Cube).filter_by(name=cube_name, owner_id=user.id).first()
    if existing_cube:
        raise CubeAlreadyExists(cube_name)

    new_cube = Cube(name=cube_name, owner_id=user.id)

    db.add(new_cube)
    db.commit()
    db.refresh(new_cube)  # to get generated ID


def remove_cube(db: Session, username: str, cube_name: str) -> None:
    user = get_user(db, username)

    cube = get_cube(db, user.id, cube_name)

    db.delete(cube)
    db.commit()


def get_cards_in_cube(db: Session, username: str, cube_name: str) -> list[Card]:
    user = get_user(db, username)

    cube = get_cube(db, user.id, cube_name)

    list_all_cards = []

    for card in cube.cards:
        list_all_cards.append(card)
    return list_all_cards


def get_cubes_of_user(db: Session, username: str) -> list[str]:
    user = get_user(db, username)

    list_all_cubes = []

    for cube in db.query(Cube).filter_by(owner_id=user.id):
        list_all_cubes.append(cube.name)
    return list_all_cubes


def add_card_to_cube(
    db: Session, username: str, cube_name: str, card_full_id: str
) -> None:
    user = get_user(db, username)

    cube = get_cube(db, user.id, cube_name)

    card = get_card(db, card_full_id)

    cube.cards.append(card)
    db.commit()


def remove_card_from_cube(
    db: Session,
    username: str,
    cube_name: str,
    card_full_id: str,
) -> None:
    user = get_user(db, username)

    cube = get_cube(db, user.id, cube_name)

    card = get_card(db, card_full_id)

    cube.cards.remove(card)
    db.commit()


if __name__ == "__main__":
    for db in get_db():
        remove_cube(db, "gauthier", "pipix")
        print("1.", get_cubes_of_user(db, "testuser"))
        print("1. Gauthier ", get_cubes_of_user(db, "gauthier"))

        create_new_cube(db, "gauthier", "pipix")

        print("2. Gauthier ", get_cubes_of_user(db, "gauthier"))

        # remove_cube(db, "gauthier", "pipix")

        print("3. Gauthier ", get_cubes_of_user(db, "gauthier"))
        add_card_to_cube(
            db, "gauthier", "pipix", "aa8f58f1-4843-4926-b3c4-98898201c216"
        )
        print("4:: ", get_cards_in_cube(db, "gauthier", "pipix"))
