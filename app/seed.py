from flask import current_app
from app.core.database import db
from app.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_admin():

    admin_email = current_app.config["ADMIN_EMAIL"]
    admin_password = current_app.config["ADMIN_PASSWORD"]

    existing_admin = User.query.filter_by(email=admin_email).first()
    if existing_admin:
        print("✅ Admin user already exists.")
        return
    hashed = bcrypt.generate_password_hash(admin_password).decode('utf-8')
    admin = User(
        username="admin",
        email=admin_email,
        password_hash=hashed,
        role="admin"
    )
    db.session.add(admin)
    db.session.commit()
    print("✅ Admin user created.")