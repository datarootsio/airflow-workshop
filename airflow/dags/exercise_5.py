
from pendulum import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


from pizzeria_plugin.timetables.my_timetable import EveryDayAtMidnightExceptWeekendsAndHolidaysTimetable


with DAG(
    "exercise-5",
    timetable=EveryDayAtMidnightExceptWeekendsAndHolidaysTimetable,
    start_date=datetime(2022, 8, 1),
    catchup=True,
) as dag:
    BashOperator(
        task_id="check",
        bash_command=(
            "echo 'data_interval_start={{ data_interval_start }};"
            "data_interval_end={{ data_interval_end }}'"
        ),
    )
