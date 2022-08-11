from pendulum import datetime

from airflow import DAG
from airflow import XComArg

from pizzeria_plugin.operators.bake_pizzas_in_batch import BakePizzasInBatch
from pizzeria_plugin.operators.wait_for_pizzas_to_be_baked import (
    WaitForPizzasToBeBaked,
)
from pizzeria_plugin.operators.deliver_pizza import (
    DeliverPizza,
)
from pizzeria_plugin.operators.wait_for_pizzas_to_be_delivered import (
    WaitForAPizzaToBeDelivered,
)


with DAG(
    "exercise-3",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    bake_batch = BakePizzasInBatch(
        task_id="bake-batch",
    )

    wait_for_baked_pizza = WaitForPizzasToBeBaked(
        task_id="wait-for-baked-pizza",
        poke_interval=5,
        order_ids="{{ ti.xcom_pull(task_ids='bake-batch') }}",
    )

    deliver = DeliverPizza.partial(task_id="deliver-pizza").expand(
        order_id=XComArg(bake_batch, key="return_value")
    )

    wait_for_delivery = WaitForAPizzaToBeDelivered.partial(
        task_id="wait-for-delivery",
        poke_interval=5,
    ).expand(order_id=XComArg(bake_batch))

    bake_batch >> wait_for_baked_pizza >> deliver >> wait_for_delivery
