from flask import jsonify, request, Blueprint
from farmapi import db
from farmapi.models import Farmer
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles
from farmapi.services import FarmerService
from markupsafe import escape
farmer_bp = Blueprint("farmer", __name__)

@farmer_bp.route("/add/farmer", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addFarmer():
    req = request.get_json()
    data = {
        "name":req.get('name'),
        "language":req.get('language'),
        "phone":req.get('phone'),
    }
    result = FarmerService.add_farmer(data)
    return jsonify(result), 200

@farmer_bp.route('/list/farmers', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listFarmers():
    farmers = FarmerService.list_farmers_dict()
    return jsonify(farmers), 200


@farmer_bp.route('/get/farmer/<int:farmer_id>', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def getFarmers(farmer_id):
    farmer = FarmerService.get_farmer_dict({"id":int(escape(farmer_id))})
    return jsonify(farmer)