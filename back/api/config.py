import os


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://mtg_user:password@localhost/mtg_cube"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")
