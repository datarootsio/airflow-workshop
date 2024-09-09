from pendulum import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    "basic-dag",
) as dag:
    echo = BashOperator(
        task_id="echo",
        bash_command="echo hello",
    )

    echo
