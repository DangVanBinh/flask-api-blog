from ..core.database import db
from .base_model import BaseModel
from ..enums.comment import CommentEnum

class Comment(BaseModel):
    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default=CommentEnum.APPROVED)  # pending | approved | rejected

    post_id = db.Column(db.Uuid, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Uuid, db.ForeignKey('users.id'), nullable=False)
