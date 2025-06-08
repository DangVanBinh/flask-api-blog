from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from ..enums.user_role import UserRole  # Import enum

def role_required(allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
                claims = get_jwt()
                role = claims.get("user", {}).get("role")

                # Admin luôn được phép truy cập
                if role == UserRole.ADMIN:
                    return fn(*args, **kwargs)

                # Kiểm tra role có trong allowed_roles không
                if role in [r.value for r in allowed_roles]:
                    return fn(*args, **kwargs)

                return jsonify({"msg": "Bạn không có quyền truy cập"}), 403
            except Exception as e:
                return jsonify({"msg": "Lỗi xác thực", "error": str(e)}), 401
        return wrapper
    return decorator
