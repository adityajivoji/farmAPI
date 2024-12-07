from farmapi.helpers import FarmHelper
from farmapi.repository import FarmRepository
from datetime import datetime
class FarmService:
    @staticmethod
    def add_farm(data):
        farmHelper = FarmHelper(
            area = data["area"],
            crop_grown=data["crop_grown"],
            sowing_date=datetime.strptime(data["sowing_date"], '%d/%m/%Y') ,
            village=data["village"],
            farmer_id=data["farmer_id"]
        )
        FarmRepository.add_farm(farmHelper)
        return "Farm Added"
    
    @staticmethod
    def list_farms(data):
        farmHelper = FarmHelper(
            farmer_id=data["farmer_id"]
        )
        farmHelpers = FarmRepository.list_farms(farmHelper)
        return farmHelpers
    
    @staticmethod
    def get_farm(data):
        farmHelper = FarmHelper(
            id=data["id"]
        )
        farmHelpers = FarmRepository.get_farm(farmHelper)
        return farmHelpers