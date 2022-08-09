from datetime import datetime, timedelta

from airflow import DAG

from pizzeria_plugin.operators.bake_one_pizza_and_wait import (
    BakeOnePizzaAndWait
)


with DAG(
    "basic_dag_with_custom_operator",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    BakeOnePizzaAndWait(
        task_id="BakeOnePizzaAndWait",
    )
