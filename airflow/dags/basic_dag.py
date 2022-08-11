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

    # https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
    use_macro = BashOperator(
        task_id="use-macro",
        bash_command=(
            "echo 'data_interval_start={{ data_interval_start }};"
            "data_interval_end={{ data_interval_end }}'"
        ),
    )

    print_date >> echo >> use_macro
    # print_date.set_downstream(echo)
    # echo.set_downstream(use_macro)
