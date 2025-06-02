from .base_model import BaseModel
from ..core.database import db

class Category(BaseModel):
    __tablename__ = 'categories'

    name = db.Column(db.String(100), unique=True, nullable=False)

    posts = db.relationship('Post', backref='category', lazy=True)