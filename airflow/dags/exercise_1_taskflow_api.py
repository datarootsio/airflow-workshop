import time

import pendulum

from airflow.decorators import dag, task

from pizzeria_plugin.hooks import pizza


@dag(
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
)
def dag_with_taskflow_api():
    @task()
    def bake_and_wait():
        pizza_order_id = pizza.bake()

        while not pizza.is_baked(pizza_order_id):
            time.sleep(1)

        return pizza_order_id

    @task()
    def deliver(order_id: str):
        pizza.send_for_delivery(int(order_id))

    order_id = bake_and_wait()
    deliver(order_id)


bake_wait_deliver_dag = dag_with_taskflow_api()
