from markupsafe import escape
from farmapi.authMiddleware.utils import requires_roles
from flask import request
from farmapi.models import Schedule
from farmapi import app, db
from flask_jwt_extended import jwt_required


@app.route("/add/schedule/<int:farm_id>", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addSchedule(farm_id):
    tempSchedule = Schedule(
        days_after_sowing=int(request.form["days_after_sowing"]),
        quantity=int(request.form["quantity"]),
        fertilizer=request.form["fertilizer"],
        quantity_unit=request.form["quantity_unit"],
        farm_id=int(escape(farm_id))
        )
    db.session.add(tempSchedule)
    db.session.commit()
    return f"Schedule added for farm with ID {farm_id}!"

@app.route('/list/schedules/<int:farm_id>', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listfarmsbyfarmid(farm_id):
    farm = Schedule.query.get(escape(int(farm_id)))
    if farm:
        return str(farm)
    return f"No farms found for Farmer ID {farm_id}."