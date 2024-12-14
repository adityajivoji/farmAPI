from farmapi.helpers import FarmerHelper
from farmapi.repository import FarmerRepository

class FarmerService:
    @staticmethod
    def add_farmer(data):
        farmerHelper = FarmerHelper(
            name = data["name"],
            phone=data["phone"],
            language=data["language"]
        )
        farmerHelper = FarmerRepository.add_farmer(farmerHelper)
        
        return farmerHelper.to_dict()
    
    @staticmethod
    def list_farmers_dict():
        farmerHelpers = FarmerRepository.list_farmers()
        return [farmer.to_dict() for farmer in  farmerHelpers]
    
    @staticmethod
    def list_farmers():
        farmerHelpers = FarmerRepository.list_farmers()
        return [farmer for farmer in  farmerHelpers]
    
    @staticmethod
    def get_farmer(data):
        farmerHelper = FarmerHelper(
            id = data["id"],

        )
        farmerHelper = FarmerRepository.get_farmer(farmerHelper)
        
        return farmerHelper
    
    @staticmethod
    def get_farmer_dict(data):
        farmerHelper = FarmerHelper(
            id = data["id"],

        )
        farmerHelper = FarmerRepository.get_farmer(farmerHelper)
        if farmerHelper:
            return farmerHelper.to_dict()
        else:
            return None