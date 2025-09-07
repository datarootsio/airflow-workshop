from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime, now

with DAG(
    "basic-dag",
    schedule_interval="0 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    echo = BashOperator(
        task_id="echo",
        bash_command="echo {{ execution_date }}",
    )
    echo2 = BashOperator(
        task_id="echo2",
        bash_command=f"echo {now('Europe/Brussels')}",
    ) 
    date = BashOperator(
        task_id="date",
        bash_command="date",
    )
    goodbye = BashOperator(
        task_id="goodbye",
        bash_command="echo goodbye"
    )

    [echo, echo2] >> date, goodbye


















from airflow.decorators import task, dag

@dag(
    schedule_interval="0 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
def taskflow_dag():
    @task.bash
    def echo():
        return "echo hello"

    @task.bash
    def show_date(prev: str):
        return "date"

    @task.bash
    def goodbye():
        return "echo goodbye"

    show_date(echo()), goodbye()

taskflow_dag()
