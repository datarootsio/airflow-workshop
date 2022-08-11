from datetime import timedelta
from typing import Optional
from pendulum import Date, DateTime, Time, timezone

from airflow.timetables.base import (
    DagRunInfo,
    DataInterval,
    TimeRestriction,
    Timetable,
)

UTC = timezone("UTC")
DELTA = timedelta(days=1)
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
        # There was a previous run on the regular schedule.
        if last_automated_data_interval is not None:
            last_end = last_automated_data_interval.end

            next_start = (last_end).set(hour=0, minute=0).replace(tzinfo=UTC)
            next_end = _get_next_end_date(next_start).replace(tzinfo=UTC)

        # This is the first ever run on the regular schedule.
        else:
            next_start = restriction.earliest

            # No start_date. Don't schedule.
            if next_start is None:
                return None

            # If the DAG has catchup=False, today is the earliest to consider.
            if not restriction.catchup:
                next_start = max(
                    next_start,
                    DateTime.combine(Date.today(), Time.min).replace(
                        tzinfo=UTC
                    ),
                )

            next_start = next_start.set(hour=0, minute=0).replace(tzinfo=UTC)
            next_end = _get_next_end_date(next_start).replace(tzinfo=UTC)

        # Over the DAG's scheduled end; don't schedule.
        if restriction.latest is not None and next_start > restriction.latest:
            return None

        return DagRunInfo.interval(start=next_start, end=next_end)


def _get_next_end_date(start: DateTime) -> DateTime:
    end = start + DELTA

    while not _is_allowed_date(end):
        end += DELTA

    return end


def _is_allowed_date(d: DateTime) -> DateTime:
    # it's weekend
    if d.weekday() >= 5:
        return False

    if d.date() in HOLIDAYS:
        return False

    return True
