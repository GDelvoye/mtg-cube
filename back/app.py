from flask import Flask
from flask_cors import CORS
from api.routes import bp

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(bp, url_prefix="/api")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == "__main__":
    app.run()
