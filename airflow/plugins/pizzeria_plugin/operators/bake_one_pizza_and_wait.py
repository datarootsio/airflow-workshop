import time

from airflow.models.baseoperator import BaseOperator

from pizzeria_plugin.hooks import pizza


class BakeOnePizzaAndWait(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        pizza_order_id = pizza.bake()

        while not pizza.is_baked(pizza_order_id):
            time.sleep(1)

        return pizza_order_id
