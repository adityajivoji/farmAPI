from markupsafe import escape
from datetime import datetime
from flask import request
from farmapi import app, db
from farmapi.models import Farm, Farmer
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles

@app.route("/add/farm/<int:farmer_id>", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addFarm(farmer_id):
    from datetime import datetime
    tempFarm = Farm(
        area=request.form["area"],
        crop_grown=request.form["crop_grown"],
        sowing_date= None if "sowing_date" not in request.form else datetime.strptime(request.form["sowing_date"], '%d/%m/%Y') ,
        village=request.form["village"],
        farmer_id=int(escape(farmer_id))
        )
    db.session.add(tempFarm)
    db.session.commit()
    return f"Farm added for farmer with ID {farmer_id}!"

@app.route('/list/farms/<int:farmer_id>', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listfarmsbyfarmerid(farmer_id):
    farmer = Farmer.query.get(escape(farmer_id))
    if farmer:
        return "<br>".join([str(farm) for farm in farmer.farm])
    return f"No farms found for Farmer ID {farmer_id}."

@app.route('/list/farms', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listFarms():
    farms = Farm.query.all()
    return "<br>".join([str(farm) for farm in farms])