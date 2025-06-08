from flask import Blueprint, request, jsonify
from app.auth.service import create_user, login_user
from marshmallow import ValidationError
from app.schemas.user_schema import RegisterSchema, LoginSchema, UserOutSchema
from app import blacklist
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    get_jwt_identity, get_jwt
)
from ..auth.middlewares import role_required
from ..enums.user_role import UserRole

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

    additional_claims = {
        "user": {
            "id": str(user.id),
            "role": user.role,
            "fullname": user.fullname
        }
    }
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
    refresh_token = create_refresh_token(identity=str(user.id), additional_claims=additional_claims)
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    })

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token)

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify(msg="Logged out")

@auth_bp.route("/aa", methods=["GET"])
@jwt_required()
@role_required([UserRole.USER])
def welcome():
    return jsonify(msg="hello")

