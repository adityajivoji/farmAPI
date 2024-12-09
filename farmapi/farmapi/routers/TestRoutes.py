from flask import Blueprint, jsonify
from farmapi.authMiddleware import requires_roles
test_routes_bp = Blueprint('testroutes', __name__)


@test_routes_bp.route('/admin', methods=['GET'])
@requires_roles('admin')
def admin_route():
    return jsonify({"msg": "Welcome, admin!"})

@test_routes_bp.route('/superadmin', methods=['GET'])
@requires_roles('superadmin')
def superadmin_route():
    return jsonify({"msg": "Welcome, superadmin!"})


@test_routes_bp.route('/user', methods=['GET'])
@requires_roles('user')
def user_route():
    return jsonify({"msg": "Welcome, user!"})