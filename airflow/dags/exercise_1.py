from pendulum import datetime

from airflow import DAG

from pizzeria_plugin.operators.bake_one_pizza_and_wait import (
    BakeOnePizzaAndWait,
)
from pizzeria_plugin.operators.deliver_pizza import (
    DeliverPizza,
)


with DAG(
    "exercise-1",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    bake_and_wait = BakeOnePizzaAndWait(
        task_id="bake-and-wait",
    )

    deliver = DeliverPizza(
        task_id="deliver",
        order_id="{{ ti.xcom_pull(task_ids='bake-and-wait') }}",
    )

    bake_and_wait >> deliver
