from farmapi.models import Farmer
from farmapi.helpers import FarmerHelper
def map_farmerhelper_to_farmer(farmer_helper: FarmerHelper) -> Farmer:
    return Farmer(
        id=farmer_helper.id,
        name=farmer_helper.name,
        phone=farmer_helper.phone,
        language=farmer_helper.language
    )


def map_farmer_to_farmerhelper(farmer: Farmer) -> FarmerHelper:
    return FarmerHelper(
        id=farmer.id,
        name=farmer.name,
        phone=farmer.phone,
        language=farmer.language,
        farms=farmer.farms
    )
