from functools import wraps
from flask import request, jsonify
from app.core.jwt_manager import decode_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"msg": "Token is missing"}), 401

        data = decode_token(token)
        if not data:
            return jsonify({"msg": "Token is invalid or expired"}), 401

        request.user = data
        return f(*args, **kwargs)

    return decorated

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = getattr(request, "user", None)
            if not user or user.get("role") not in roles:
                return jsonify({"msg": "Forbidden"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
