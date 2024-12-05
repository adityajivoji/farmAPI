from datetime import datetime
from farmapi.authMiddleware.utils import requires_roles
from farmapi.models import Farmer, Schedule, Farm
from farmapi import app
from flask_jwt_extended import jwt_required

@app.route("/get_view/todaytomorrow", methods=['GET'])
@jwt_required()
@requires_roles("superdamin", "admin", "user")
def viewTodayTomorrow():
    from datetime import datetime, timedelta
    today = datetime.today()
    schedules = Schedule.query.all()
    returnable = []
    for schedule in schedules:
        
        das = schedule.days_after_sowing
        farm_id = schedule.farm_id
        farm = Farm.query.get(farm_id)
        dateDiff = today - farm.sowing_date
        print(das, today, farm.sowing_date)
        if 0 <= dateDiff.days - das < 2:
            returnable.append(
                (
                    farm.sowing_date + timedelta(days=das),
                    farm.id,
                    schedule.id
                    )
            )
    return returnable

        
@app.route("/get_view/all_farmer_growing_crop", methods=['GET'])
@jwt_required()
@requires_roles("superdamin", "admin", "user")
def getFarmerGrowingCrop():
    farmers = Farmer.query.all()
    returnable = []
    unique_ids = set()
    for farmer in farmers:
        farms = farmer.farm
        for farm in farms:
            if farm.sowing_date != datetime(1990, 1, 1):
                if farmer.id not in unique_ids:
                    unique_ids.add(farmer.id)
                    returnable.append(
                        (
                            farmer.id,
                            farmer.name
                        )
                    )
                
    return returnable

prices = {
    "NPA": 400
}

@app.route("/get_view/bills/<int:farmer_id>", methods=['GET'])
@jwt_required()
@requires_roles("superdamin", "admin", "user")
def generateBills(farmer_id):
    farmer = Farmer.query.get(farmer_id)
    farms = farmer.farm
    total = 0
    for farm in farms:
        schedules = farm.schedule
        for schedule in schedules:
            total += prices[schedule.fertilizer] * schedule.quantity
            print(prices[schedule.fertilizer], schedule.quantity)
    return str(total)