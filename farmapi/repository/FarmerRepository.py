from farmapi import db
from farmapi.helpers import FarmerHelper
from farmapi.mappers.FarmerMapper import map_farmer_to_farmerhelper, map_farmerhelper_to_farmer
from farmapi.models import Farmer

class FarmerRepository:
    @staticmethod
    def add_farmer(farmerHelper: FarmerHelper):
        farmer = map_farmerhelper_to_farmer(farmerHelper)
        db.session.add(farmer)
        db.session.commit()
    
    @staticmethod
    def list_farmers():
        farmers = Farmer.query.all()
        if farmers:
            return [map_farmer_to_farmerhelper(farmer).to_dict() for farmer in farmers]
        else:
            []
    
    @staticmethod
    def get_farmer(farmerHelper: FarmerHelper):
        farmer = map_farmerhelper_to_farmer(farmerHelper)
        farmers = Farmer.query.filter_by(id=farmer.id).first()  # Fetch the first matching record

        if farmers:  # Check if a record exists
            ret = map_farmer_to_farmerhelper(farmers)  # Use the fetched farmer            
            return ret
        else:
            return None
