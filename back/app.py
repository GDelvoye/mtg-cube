from flask import Flask, request, jsonify
from flask_cors import CORS
from src.naming import generate_visualization_infos_official_set


app = Flask(__name__)
CORS(app)


@app.route("/visualization-official", methods=["POST"])
def visualize_official():
    """Route asking data for visualization of an official set."""
    set_name = request.get_json()["set_name"]
    print(set_name)

    return jsonify(generate_visualization_infos_official_set(set_name))


if __name__ == "__main__":
    app.run(debug=True)
