from airflow.plugins_manager import AirflowPlugin

from pizzeria_plugin.timetables.my_timetable import (
    EveryDayAtMidnightExceptWeekendsAndHolidaysTimetable,
)


class PizzeriaPlugin(AirflowPlugin):
    name = "pizzeria_plugin"

    timetables = [EveryDayAtMidnightExceptWeekendsAndHolidaysTimetable]
