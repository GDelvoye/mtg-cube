from flask import Flask
from flask_jwt_extended import JWTManager
from api.config import Config


jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)

    from api.routes.auth import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
