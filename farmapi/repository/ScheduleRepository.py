from farmapi import db
from farmapi.helpers import ScheduleHelper
from farmapi.mappers import map_schedulehelper_to_schedule, map_schedule_to_schedulehelper
from farmapi.models import Farm, Schedule

class ScheduleRepository:
    @staticmethod
    def add_schedule(scheduleHelper: ScheduleHelper):
        farm = map_schedulehelper_to_schedule(scheduleHelper)
        db.session.add(farm)
        db.session.commit()
    
    @staticmethod
    def list_schedules(scheduleHelper: ScheduleHelper):
        schedule = map_schedulehelper_to_schedule(scheduleHelper)
        schedules = Farm.query.filter_by(id=schedule.farm_id).first()
        if schedules:
            schedules = schedules.schedule
            return [map_schedule_to_schedulehelper(schedule).to_dict() for schedule in schedules]
        else:
            return []
        
    @staticmethod
    def get_all_schedules():
        schedules = Schedule.query.all()
        if schedules:
            schedules = schedules
            return [map_schedule_to_schedulehelper(schedule).to_dict() for schedule in schedules]
        else:
            return []