from datetime import datetime

from flask import Blueprint, jsonify
from farmapi.authMiddleware.utils import requires_roles
from farmapi.models import Farmer, Schedule, Farm
from flask_jwt_extended import jwt_required
from farmapi.services import ScheduleService, FarmService, FarmerService
views_bp = Blueprint('views', __name__)


class ViewService:
    @staticmethod
    def viewTodayTomorrow():
        from datetime import datetime, timedelta
        today = datetime.today()
        schedules = ScheduleService.get_all_schedule()
        returnable = []
        for schedule in schedules:
            
            das = schedule.days_after_sowing
            farm_id = schedule.farm_id
            farm = FarmService.get_farm({"id": farm_id})
            if farm != None and farm.sowing_date:
                dateDiff = today - farm.sowing_date
                if 0 <= dateDiff.days - das < 2:
                    returnable.append(
                        {
                            "Date":farm.sowing_date + timedelta(days=das),
                            "Farm Id":farm.id,
                            "Schedule Id":schedule.id
                        }
                    )
            
        return returnable

            
    @staticmethod
    def getFarmerGrowingCrop():
        farmers = FarmerService.list_farmers()
        returnable = []
        unique_ids = set()
        for farmer in farmers:
            farms = farmer.farms
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

    @staticmethod
    def generateBills(farmer_id):
        print("In view service", farmer_id)
        prices = {
            "NPA": 400
        }
        farmer = FarmerService.get_farmer({"id":farmer_id})
        if farmer:
            farms = farmer.farms
            total = 0
            if farms:
                for farm in farms:
                    schedules = farm.schedule
                    for schedule in schedules:
                        total += prices[schedule.fertilizer] * schedule.quantity
                return total
            else:
                return "No farms Found"
        else:
            return "No Farmer Found"