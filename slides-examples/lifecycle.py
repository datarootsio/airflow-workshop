from pendulum import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    "basic-dag",
    schedule_interval="5 4 * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    print_date = BashOperator(
        task_id="print-date",
        bash_command="date",
    )

    echo = BashOperator(
        task_id="echo",
        bash_command="echo hello",
    )

    print_date >> echo
    # print_date.set_downstream(echo)
