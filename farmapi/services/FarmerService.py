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
        FarmerRepository.add_farmer(farmerHelper)
        return "Farmer Added"
    
    @staticmethod
    def list_farmers():
        farmerHelpers = FarmerRepository.list_farmers()
        return farmerHelpers
    
    @staticmethod
    def get_farmer(data):
        print("in farmer service", data["id"],)
        farmerHelper = FarmerHelper(
            id = data["id"],

        )
        farmerHelper = FarmerRepository.get_farmer(farmerHelper)
        print("farmer service", farmerHelper.farms)
        return farmerHelper