from flask import Blueprint, Response, request, jsonify
from database.models import User
from database.connection import SessionLocal
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    hashed = generate_password_hash(password)
    db = SessionLocal()
    try:
        user = User(username=username)
        user.password_hash = hashed
        db.add(user)
        db.commit()
        return jsonify({"msg": "User created"}), 201
    except IntegrityError:
        db.rollback()
        return jsonify({"msg": "User already exists"}), 400
    finally:
        db.close()


@auth_bp.route("/login", methods=["POST"])
def login() -> Response:
    data = request.get_json()
    print("DATA", data)
    username = data["username"]
    password = data["password"]
    print("USERNAME", username)

    db = SessionLocal()
    user = db.query(User).filter_by(username=username).first()
    users = db.query(User).all()
    for usera in users:
        print(
            f"USERS |||| Id: {usera.id}, name: {usera.username}, pass: {usera.password_hash}"
        )
    db.close()

    if user is None or not check_password_hash(user.password_hash, password):
        print("COIN COIN")
        result = {"msg": "Invalid identifiers."}
        return jsonify(result)  # , 401

    # JWT creation for user
    print("GOOOOD")
    access_token = create_access_token(identity=user.id)
    print("ACCESS TOKEN", access_token)

    return jsonify({"token": access_token, "username": username}), 200
