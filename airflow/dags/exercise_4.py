from pendulum import datetime

from airflow import DAG

from pizzeria_plugin.operators.order_pizza import OrderPizza


with DAG(
    "exercise-4",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    OrderPizza(
        task_id="order-pizza",
        pizza_type="{{ dag_run.conf['pizza_type'] }}",
    )
