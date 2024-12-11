from farmapi import db
from farmapi.helpers import FarmHelper
from farmapi.mappers.FarmMapper import map_farm_to_farmhelper, map_farmhelper_to_farm
from farmapi.models import Farm, Farmer

class FarmRepository:
    @staticmethod
    def add_farm(farmHelper: FarmHelper):
        farm = map_farmhelper_to_farm(farmHelper)
        db.session.add(farm)
        db.session.commit()
        return map_farm_to_farmhelper(farm)
    
    @staticmethod
    def list_farms(farmHelper: FarmHelper):
        farm = map_farmhelper_to_farm(farmHelper)
        farms = Farmer.query.filter_by(id=farm.farmer_id).first()
        if farms:
            farms = farms.farms
            return [map_farm_to_farmhelper(farm) for farm in farms]
        else:
            return []
    
    @staticmethod
    def get_farm(farmHelper: FarmHelper):
        farm = map_farmhelper_to_farm(farmHelper)
        farm = Farm.query.filter_by(id=farm.id).first()
        if farm:
            return map_farm_to_farmhelper(farm)
        else:
            return None