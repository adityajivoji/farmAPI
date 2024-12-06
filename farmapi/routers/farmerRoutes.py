from flask import jsonify, request, Blueprint
from farmapi import db
from farmapi.models import Farmer
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles
from farmapi.services import FarmerService

farmer_bp = Blueprint("farmer", __name__)

@farmer_bp.route("/add/farmer", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addFarmer():
    data = {
        "name":request.form["name"],
        "language":request.form["language"],
        "phone":request.form["phone"]
    }
    result = FarmerService.add_farmer(data)
    return jsonify(result), 200

@farmer_bp.route('/list/farmers', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listFarmers():
    farmers = FarmerService.list_farmers()
    return jsonify(farmers), 200