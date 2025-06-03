from app.models.user import User
from app.core.database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_user(username, email, password):
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password_hash=hashed)
    db.session.add(user)
    db.session.commit()
    return user

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return user
    return None
