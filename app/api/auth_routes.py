from flask import Blueprint, request, jsonify
from app.auth.service import create_user, login_user
from app.core.jwt_manager import create_access_token
from marshmallow import ValidationError
from app.schemas.user_schema import RegisterSchema, LoginSchema, UserOutSchema

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = RegisterSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    user = create_user(data["username"], data["email"], data["password"])
    return UserOutSchema().dump(user), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = LoginSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = login_user(data["username"], data["password"])
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(str(user.id), user.role)
    return jsonify({"access_token": token})
