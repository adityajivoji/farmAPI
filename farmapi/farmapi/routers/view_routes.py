from markupsafe import escape
from flask import Blueprint, jsonify
from farmapi.authMiddleware.utils import requires_roles
from flask_jwt_extended import jwt_required
from farmapi.services import ViewService
views_bp = Blueprint('views', __name__)

@views_bp.route("/get_view/todaytomorrow", methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def viewTodayTomorrow():
    returnable = ViewService.viewTodayTomorrow()
    return jsonify(returnable)

        
@views_bp.route("/get_view/all_farmer_growing_crop", methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def getFarmerGrowingCrop():
    returnable = ViewService.getFarmerGrowingCrop()       
    return jsonify(returnable)

@views_bp.route("/get_view/bills/<int:farmer_id>", methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def generateBills(farmer_id):
    return jsonify(str(ViewService.generateBills(escape(farmer_id))))