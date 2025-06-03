import uuid
from sqlalchemy.dialects.postgresql import UUID
from ..core.database import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # Không tạo bảng cho class này

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ative = db.Column(db.Boolean, default=True)