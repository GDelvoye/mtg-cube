from flask import Flask, request, jsonify
from src.naming import generate_visualization_infos_official_set


app = Flask(__name__)


@app.route("/visualize-official", methods=["POST"])
def visualize_official():
    """Route asking data for visualization of an official set."""
    set_name = request.get_json()

    return jsonify(generate_visualization_infos_official_set(set_name))


if __name__ == "__main__":
    app.run(debug=True)
