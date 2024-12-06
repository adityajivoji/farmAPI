from datetime import datetime
from farmapi.models import Farm
from farmapi.helpers import FarmHelper
def map_farmhelper_to_farm(farm_helper: FarmHelper) -> Farm:
    return Farm(
        id=farm_helper.id,
        area=farm_helper.area,
        crop_grown=farm_helper.crop_grown,
        sowing_date=None if not farm_helper.sowing_date else datetime.strptime(farm_helper.sowing_date, '%d/%m/%Y') ,
        village=farm_helper.village,
        farmer_id=farm_helper.farmer_id
    )


def map_farm_to_farmhelper(farm: Farm) -> FarmHelper:
    return FarmHelper(
        id=farm.id,
        area=farm.area,
        crop_grown=farm.crop_grown,
        sowing_date=farm.sowing_date,
        village=farm.village,
        farmer_id=farm.farmer_id,
        schedule=farm.schedule
    )
