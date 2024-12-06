from markupsafe import escape
from datetime import datetime
from flask import request, Blueprint
from farmapi import db
from farmapi.models import Farm, Farmer
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles
from farmapi.services import FarmService

farm_bp = Blueprint('farm', __name__)

@farm_bp.route("/add/farm/<int:farmer_id>", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def add_farm(farmer_id):
    data = {
        "area":request.form["area"],
        "crop_grown":request.form["crop_grown"],
        "sowing_date": request.form["sowing_date"],
        "village":request.form["village"],
        "farmer_id":int(escape(farmer_id))
    }
    result = FarmService.add_farm(data)

    return result, 200

@farm_bp.route('/list/farms/<int:farmer_id>', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listfarmsbyfarmerid(farmer_id):
    data = {
        "farmer_id":int(escape(farmer_id))
    }
    result = FarmService.list_farms(data)

    return result

