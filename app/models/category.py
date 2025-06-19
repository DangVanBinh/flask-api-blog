from .base_model import BaseModel
from ..core.database import db

class Category(BaseModel):
    __tablename__ = 'categories'

    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)

    posts = db.relationship('Post', backref='category', lazy=True)