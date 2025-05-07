from flask import Blueprint, Response, jsonify, request

from database.cube.create_cube import (
    add_card_to_cube,
    create_new_cube,
    get_cards_in_cube,
    remove_card_from_cube,
    remove_cube,
)
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database.session import get_db


cube_bp = Blueprint("cube", __name__)


@cube_bp.route("/create-cube", methods=["POST"])
def create_cube() -> Response:
    data = request.get_json()
    username = data["username"]
    cube_name = data["cube_name"]

    if not username or not cube_name:
        return jsonify({"error": "Missing username or cube_name"}), 400

    db: Session = get_db()
    try:
        create_new_cube(db, username, cube_name)
        return jsonify({"message": f"Cube '{cube_name}' created."}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except SQLAlchemyError:
        db.rollback()
        return jsonify({"error": "Database error"}), 500


@cube_bp.route("/delete-cube", methods=["POST"])
def delete_cube() -> Response:
    data = request.get_json()
    username = data["username"]
    cube_name = data["cube_name"]

    if not username or not cube_name:
        return jsonify({"error": "Missing username or cube_name"}), 400

    db: Session = get_db()
    try:
        remove_cube(db, username, cube_name)
        return jsonify({"message": f"Cube '{cube_name}' deleted."}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except SQLAlchemyError:
        db.rollback()
        return jsonify({"error": "Database error"}), 500


@cube_bp.route("/display-cards-in-cube", methods=["POST"])
def display_cards_in_cube() -> Response:
    data = request.get_json()
    username = data["username"]
    cube_name = data["cube_name"]

    if not username or not cube_name:
        return jsonify({"error": "Missing username or cube_name"}), 400

    db: Session = get_db()
    try:
        list_cards = get_cards_in_cube(db, username, cube_name)
        result = [card.to_dict() for card in list_cards]
        return jsonify(result), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except SQLAlchemyError:
        db.rollback()
        return jsonify({"error": "Database error"}), 500


@cube_bp.route("/add-card-in-cube", methods=["POST"])
def add_card_to_cube_endpoint() -> Response:
    data = request.get_json()
    username = data["username"]
    cube_name = data["cube_name"]
    card_full_id = data["card_full_id"]

    if not username or not cube_name or not card_full_id:
        return jsonify({"error": "Missing username, cube_name ore full_id_card"}), 400

    db: Session = get_db()
    try:
        add_card_to_cube(db, username, cube_name, card_full_id)
        return jsonify(
            {"message": f"Card '{card_full_id}' added to cube '{cube_name}'."}
        ), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except SQLAlchemyError:
        db.rollback()
        return jsonify({"error": "Database error"}), 500


@cube_bp.route("/remove-card-from-cube", methods=["POST"])
def remove_card_from_cube_endpoint() -> Response:
    data = request.get_json()
    username = data["username"]
    cube_name = data["cube_name"]
    card_full_id = data["card_full_id"]

    if not username or not cube_name or not card_full_id:
        return jsonify({"error": "Missing username, cube_name ore full_id_card"}), 400

    db: Session = get_db()
    try:
        remove_card_from_cube(db, username, cube_name, card_full_id)
        return jsonify(
            {"message": f"Card '{card_full_id}' removed from cube '{cube_name}'."}
        ), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except SQLAlchemyError:
        db.rollback()
        return jsonify({"error": "Database error"}), 500
