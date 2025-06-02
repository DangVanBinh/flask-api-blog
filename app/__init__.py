from flask import Flask
from app.core.database import db
from config import Config
from app.models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Tạo bảng trong DB
    # from app.api.auth_routes import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app