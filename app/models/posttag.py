from ..core.database import db
from .base_model import BaseModel

class PostTag(BaseModel):
    __tablename__ = 'post_tags'

    post_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('tags.id'), primary_key=True)
