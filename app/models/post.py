from ..core.database import db
from .base_model import BaseModel

class Post(BaseModel):
    __tablename__ = 'posts'

    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Uuid, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Uuid, db.ForeignKey('categories.id'), nullable=True)

    comments = db.relationship('Comment', backref='post', lazy=True)
