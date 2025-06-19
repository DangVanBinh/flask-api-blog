from ..core.database import db
from .base_model import BaseModel
from ..enums.user_role import UserRole

class User(BaseModel):
    __tablename__ = 'users'

    fullname = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    avatar_url = db.Column(db.String(255))
    bio = db.Column(db.Text)
    role = db.Column(db.String(20), default=UserRole.USER)

    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)
    likes = db.relationship("Like", backref="user", lazy=True)