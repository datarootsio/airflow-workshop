from pendulum import datetime

from airflow import DAG

from pizzeria_plugin.operators.bake_pizzas_in_batch import BakePizzasInBatch
from pizzeria_plugin.operators.wait_for_pizzas_to_be_baked import (
    WaitForPizzasToBeBaked,
)


with DAG(
    "exercise-2",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    bake_batch = BakePizzasInBatch(
        task_id="bake-batch",
    )

    wait_for_baked_pizza = WaitForPizzasToBeBaked(
        task_id="wait-for-baked-pizza",
        order_ids="{{ ti.xcom_pull(task_ids='bake-batch') }}",
    )

    bake_batch >> wait_for_baked_pizza
