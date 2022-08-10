from pendulum import datetime

from airflow import DAG

# Today we are datetime(2022, 3, 1)
with DAG(
    "my-dag-1",
    schedule_interval="0 0 * * *",  # at 00:00 everyday
    start_date=datetime(2022, 1, 1),
    catchup=True,
) as dag:
    ...


# Today we are datetime(2022, 3, 1)
with DAG(
    "my-dag-1",
    schedule_interval="0 0 * * *",  # at 00:00 everyday
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    ...


with DAG(
    "my-dag-1",
    schedule_interval="0 0 * * *",  # at 00:00 everyday
    timetable=MyTimetable(),
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2022, 1, 10),
    catchup=False,
) as dag:
    ...



# Using Macros
print_date = BashOperator(
        task_id="print-date",
        bash_command="echo {{ execution_date }}",
    )

# Using XCOM
xcom_example = BashOperator(
    task_id="xcom-example",
    bash_command="echo {{ ti.xcom_pull(task_ids='my-task', key='my-key') }}",
)



