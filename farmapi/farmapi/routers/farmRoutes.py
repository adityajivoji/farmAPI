from markupsafe import escape
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles
from farmapi.services import FarmService

farm_bp = Blueprint('farm', __name__)

@farm_bp.route("/add/farm/<int:farmer_id>", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def add_farm(farmer_id):
    req = request.get_json()
    data = {
        "area":req.get('area'),
        "crop_grown":req.get('crop_grown'),
        "sowing_date": req.get('sowing_date'),
        "village":req.get('village'),
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
