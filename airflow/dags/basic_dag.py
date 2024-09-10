from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

with DAG(
    "basic-dag",
    schedule_interval="5 4 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    echo = BashOperator(
        task_id="echo",
        bash_command="echo hello",
    )
