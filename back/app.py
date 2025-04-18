from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from src.naming import generate_visualization_infos_official_set, get_stat_about_regex


app = Flask(__name__)
CORS(app)


@app.route("/hello", methods=["GET"])
def hello():
    return {"text": "coucou"}


@app.route("/visualization-official", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
