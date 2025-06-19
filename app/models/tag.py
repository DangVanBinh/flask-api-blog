from ..core.database import db
from .base_model import BaseModel

class Tag(BaseModel):
    __tablename__ = 'tags'

    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))

    posts = db.relationship("Post", secondary="post_tags", back_populates="tags")
