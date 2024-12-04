from markupsafe import escape
from datetime import datetime
from flask import request
from farmapi.models import Farmer, Farm, Schedule
from farmapi import app, db

@app.route("/hello", methods=['POST'])
def helloByName():
    data = request.get_json()
    return f"hello, {data['name']}"

@app.route("/add/farmer", methods=['POST'])
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
def listFarmers():
    farmers = Farmer.query.all()
    return "<br>".join([str(farmer) for farmer in farmers])

@app.route("/add/farm/<int:farmer_id>", methods=['POST'])
def addFarm(farmer_id):
    from datetime import datetime
    tempFarm = Farm(
        area=request.form["area"],
        crop_grown=request.form["crop_grown"],
        sowing_date=datetime.strptime(request.form["sowing_date"], '%d/%m/%Y'),
        village=request.form["village"],
        farmer_id=int(escape(farmer_id))
        )
    db.session.add(tempFarm)
    db.session.commit()
    return f"Farm added for farmer with ID {farmer_id}!"

@app.route('/list/farms/<int:farmer_id>', methods=['GET'])
def listfarmsbyfarmerid(farmer_id):
    farmer = Farmer.query.get(escape(farmer_id))
    if farmer:
        return "<br>".join([str(farm) for farm in farmer.farm])
    return f"No farms found for Farmer ID {farmer_id}."

@app.route('/list/farms', methods=['GET'])
def listFarms():
    farms = Farm.query.all()
    return "<br>".join([str(farm) for farm in farms])

@app.route("/add/schedule/<int:farm_id>", methods=['POST'])
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
def listfarmsbyfarmid(farm_id):
    farm = Schedule.query.get(escape(int(farm_id)))
    if farm:
        return str(farm)
    return f"No farms found for Farmer ID {farm_id}."


@app.route("/get_view/todaytomorrow", methods=['GET'])
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

        
@app.route("/get_view/all_farmer_growing_crop")
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