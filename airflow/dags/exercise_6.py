from pendulum import datetime

from airflow import DAG

from pizzeria_plugin.deferrable_operator import RandomSensor


with DAG(
    "exercise-6",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    RandomSensor(task_id="random-1", chance=0.1)
    RandomSensor(task_id="random-2", chance=0.2)
