from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles
from farmapi.services import UserService

userregister_bp = Blueprint('userregister', __name__)

@userregister_bp.route("/register/admin", methods=['POST'])
@jwt_required()
@requires_roles("superadmin")
def register_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    roles = data.get('roles').strip().split(',')
    result = UserService.create_admin(username=username, password=password, email=email, roles = roles)
    print(result)
    print(type(result))
    return jsonify(result), 200

@userregister_bp.route("/register/superadmin", methods=['POST'])
@jwt_required()
@requires_roles("superadmin")
def register_superadmin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    roles = data.get('roles').strip().split(',')
    result = UserService.create_superadmin(username=username, password=password, email=email, roles = roles)
    return jsonify(result), 200


@userregister_bp.route("/register/user", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    roles = data.get('roles').strip().split(',')
    result = UserService.create_user(username=username, password=password, email=email, roles = roles)
    return jsonify(result), 200