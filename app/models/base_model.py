from ..core.database import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # Không tạo bảng cho class này

    id = db.Column(db.Uuid, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    ative = db.Column(db.Boolean, default=True)