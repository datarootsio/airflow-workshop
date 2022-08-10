from unittest.mock import patch

from pendulum import datetime

from airflow import DAG

from pizzeria_plugin.operators.bake_pizzas_in_batch import BakePizzasInBatch


def test_bake_batch_basic():
    with patch("pizzeria_plugin.hooks.pizza.bake_batch", return_value=[1]):
        dag = DAG("exercise-1", start_date=datetime(2022, 1, 1),)
        order_ids = BakePizzasInBatch(task_id="task", dag=dag).execute(None)

    assert len(order_ids) != 0
