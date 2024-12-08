from markupsafe import escape
from farmapi.authMiddleware.utils import requires_roles
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from farmapi.services import ScheduleService

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route("/add/schedule/<int:farm_id>", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addSchedule(farm_id):
    data = {
        "days_after_sowing":int(request.form["days_after_sowing"]),
        "quantity":int(request.form["quantity"]),
        "fertilizer":request.form["fertilizer"],
        "quantity_unit":request.form["quantity_unit"],
        "farm_id":int(escape(farm_id))
    }
    result = ScheduleService.add_schedule(data)
    return jsonify(result)

@schedule_bp.route('/list/schedules/<int:farm_id>', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listfarmsbyfarmid(farm_id):
    data = {
        "farm_id":int(escape(farm_id))
    }
    result = ScheduleService.list_schedules(data)
    return jsonify(result), 200