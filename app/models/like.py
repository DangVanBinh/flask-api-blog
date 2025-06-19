from ..core.database import db
from .base_model import BaseModel

class Like(BaseModel):
    __tablename__ = 'likes'

    post_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint('post_id', 'user_id', name='unique_user_like'),)
