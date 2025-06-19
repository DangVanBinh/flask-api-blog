from enum import Enum

class CommentEnum(str,Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
