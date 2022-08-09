from pendulum import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    "basic-dag",
    schedule_interval="5 4 * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    BashOperator(
        task_id="print-date",
        bash_command="date",
    )
