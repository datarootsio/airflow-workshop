from pendulum import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    "basic-branches",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    print_date = BashOperator(
        task_id="print-date",
        bash_command="date",
    )

    echo_bar = BashOperator(
        task_id="echo-bar",
        bash_command="echo bar",
    )

    wait_1 = BashOperator(task_id="wait-1", bash_command="sleep 1")

    wait_10 = BashOperator(task_id="wait-10", bash_command="sleep 10")

    branch_1 = BashOperator(task_id="branch-1", bash_command="echo branch-1")

    branch_2 = BashOperator(task_id="branch-2", bash_command="echo branch-2")

    echo_foo = BashOperator(
        task_id="echo-foo",
        bash_command="echo foo",
    )

    print_date >> [wait_1, wait_10] >> echo_bar
    echo_bar >> branch_1 >> echo_foo
    echo_bar >> branch_2
