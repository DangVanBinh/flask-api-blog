from flask import Flask
from app.core.database import db
from config import Config
from app.models import *
from app.seed import create_admin
from flask_migrate import Migrate
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    Migrate(app, db)

    with app.app_context():
        db.create_all()  # Tạo bảng trong DB
        create_admin()
    from app.api.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app