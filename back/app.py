from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from api.config import Config
from src.querying.query import get_all_sets
from src.naming import generate_visualization_infos_official_set, get_stat_about_regex
from src.querying.advanced_query import search
from api.routes.auth import auth_bp
from api.routes.cube import cube_bp


app = Flask(__name__)
CORS(app)

jwt = JWTManager()


app.config.from_object(Config)

jwt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cube_bp, url_prefix="/cube")


@app.route("/hello", methods=["GET"])
def hello():
    return {"text": "coucou"}


@app.route("/get-cube-summary", methods=["POST"])
def visualize_official() -> Response:
    """Route asking data for visualization of an official set."""
    set_name = request.get_json()["setName"]
    print(set_name)
    result = generate_visualization_infos_official_set(set_name)
    print(result)
    return jsonify(result)


@app.route("/cube-text-request", methods=["POST"])
def cube_text_request() -> Response:
    """Given a set and a regex, ask for stat those regex on set."""
    payload = request.get_json()
    print(payload)
    regex = payload["text"]
    set_name = payload["setName"]

    return jsonify(get_stat_about_regex(regex, set_name))


@app.route("/search-cards", methods=["POST"])
def search_cards() -> Response:
    filters = request.get_json()
    print("FILTERS FILTERS", filters)
    if not filters:
        return jsonify({"error": "No filters provided"}), 400

    result = search(filters)
    resres = [card.to_dict() for card in result]
    # print(resres)
    return jsonify(resres)


@app.route("/fetch-app-info", methods=["GET"])
def fetch_app_info() -> Response:
    result = {
        "availableSets": get_all_sets(),
        "totalCardsNumber": 47890,
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
