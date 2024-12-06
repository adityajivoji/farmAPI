from farmapi.helpers import ScheduleHelper
from farmapi.repository import ScheduleRepository

class ScheduleService:
    @staticmethod
    def add_schedule(data):
        scheduleHelper = ScheduleHelper(
            days_after_sowing = data["days_after_sowing"],
            quantity=data["quantity"],
            fertilizer=data["fertilizer"],
            quantity_unit=data["quantity_unit"],
            farm_id=data["farm_id"]
        )
        ScheduleRepository.add_schedule(scheduleHelper)
        return "Schedule Added"
    
    @staticmethod
    def list_schedules(data):
        scheduleHelper = ScheduleHelper(
            farm_id=data["farm_id"]
        )
        scheduleHelpers = ScheduleRepository.list_schedules(scheduleHelper)
        return scheduleHelpers
    
    @staticmethod
    def get_all_schedule():
        scheduleHelpers = ScheduleRepository.get_all_schedules()
        return scheduleHelpers
        