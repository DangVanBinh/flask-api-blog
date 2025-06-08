from flask import Flask
from app.core.database import db
from config import Config
from app.models import *
from app.seed import create_admin
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

jwt = JWTManager()
blacklist = set()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    Migrate(app, db)
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in blacklist

    with app.app_context():
        db.create_all()  # Tạo bảng trong DB
        create_admin()
    from app.api.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app