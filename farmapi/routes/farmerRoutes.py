from flask import request
from farmapi import app, db
from farmapi.models import Farmer
from flask_jwt_extended import jwt_required
from farmapi.authMiddleware.utils import requires_roles

@app.route("/add/farmer", methods=['POST'])
@jwt_required()
@requires_roles("superadmin", "admin")
def addFarmer():
    tempFarmer = Farmer(
        name=request.form["name"],
        language=request.form["language"],
        phone=request.form["phone"]
        )
    db.session.add(tempFarmer)
    db.session.commit()
    return "Farmer Added!!"

@app.route('/list/farmers', methods=['GET'])
@jwt_required()
@requires_roles("superadmin", "admin", "user")
def listFarmers():
    farmers = Farmer.query.all()
    return "<br>".join([str(farmer) for farmer in farmers])