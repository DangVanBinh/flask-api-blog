from ..core.database import db
from .base_model import BaseModel

class Comment(BaseModel):
    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)

    post_id = db.Column(db.Uuid, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Uuid, db.ForeignKey('users.id'), nullable=False)
