from flask import Blueprint, request, jsonify
from postgresql_db.database import SessionLocal, User
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
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    db = SessionLocal()
    user = db.query(User).filter_by(username=username).first()
    db.close()

    if user is None or not check_password_hash(user.password_hash, password):
        return jsonify({"msg", "Invalid identifiers."}), 401

    # JWT creation for user
    access_token = create_access_token(identity=user.id)

    return jsonify(access_token=access_token), 200
