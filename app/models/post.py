from ..core.database import db
from .base_model import BaseModel

class Post(BaseModel):
    __tablename__ = 'posts'

    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    thumbnail_url = db.Column(db.String(255))

    published = db.Column(db.Boolean, default=False)
    published_at = db.Column(db.DateTime)

    is_featured = db.Column(db.Boolean, default=False)
    view_count = db.Column(db.Integer, default=0)
    like_count = db.Column(db.Integer, default=0)
    reading_time = db.Column(db.Integer)
    seo_title = db.Column(db.String(255))
    seo_description = db.Column(db.String(300))

    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('categories.id'), nullable=True)

    tags = db.relationship("Tag", secondary="post_tags", back_populates="posts")
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='post', lazy=True, cascade="all, delete-orphan")
