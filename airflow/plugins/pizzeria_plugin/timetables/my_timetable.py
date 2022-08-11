from typing import Optional
from pendulum import Date, DateTime, Time, timezone

from airflow.timetables.base import (
    DagRunInfo,
    DataInterval,
    TimeRestriction,
    Timetable,
)

UTC = timezone("UTC")
HOLIDAYS = [
    Date(2022, 8, 2),
    Date(2022, 8, 3),
    Date(2022, 8, 9),
    Date(2022, 8, 25),
]


class EveryDayAtMidnightExceptWeekendsAndHolidaysTimetable(Timetable):
    def infer_manual_data_interval(self, run_after: DateTime) -> DataInterval:
        # Don't implement
        pass

    def next_dagrun_info(
        self,
        *,
        last_automated_data_interval: Optional[DataInterval],
        restriction: TimeRestriction,
    ) -> Optional[DagRunInfo]:
        # implement this function
        # use https://www.astronomer.io/guides/scheduling-in-airflow/ > scroll to Timetables
        # has a guideline
        pass
