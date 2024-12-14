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
        
        return ScheduleRepository.add_schedule(scheduleHelper).to_dict()
    
    @staticmethod
    def list_schedules_dict(data):
        scheduleHelper = ScheduleHelper(
            farm_id=data["farm_id"]
        )
        scheduleHelpers = ScheduleRepository.list_schedules(scheduleHelper)
        return [schedule.to_dict() for schedule in scheduleHelpers]
    
    @staticmethod
    def get_all_schedule():
        scheduleHelpers = ScheduleRepository.get_all_schedules()
        return scheduleHelpers
        