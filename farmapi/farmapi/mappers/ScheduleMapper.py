from farmapi.models import Schedule
from farmapi.helpers import ScheduleHelper
def map_schedulehelper_to_schedule(schedule_helper: ScheduleHelper) -> Schedule:
    return Schedule(
        days_after_sowing=schedule_helper.days_after_sowing,
        fertilizer=schedule_helper.fertilizer,
        quantity=schedule_helper.quantity,
        quantity_unit=schedule_helper.quantity_unit,
        farm_id=schedule_helper.farm_id
    )


def map_schedule_to_schedulehelper(schedule: Schedule) -> ScheduleHelper:
    return ScheduleHelper(
        id=schedule.id,
        days_after_sowing=schedule.days_after_sowing,
        fertilizer=schedule.fertilizer,
        quantity=schedule.quantity,
        quantity_unit=schedule.quantity_unit,
        farm_id=schedule.farm_id
    )
