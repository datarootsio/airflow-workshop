from typing import List
import json

from airflow.sensors.base_sensor_operator import BaseSensorOperator

from pizzeria_plugin.hooks import pizza


class WaitForPizzasToBeBaked(BaseSensorOperator):
    template_fields = ["order_ids"]

    def __init__(self, order_ids: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.order_ids = order_ids

    def poke(self, context):
        order_ids_parsed: List[int] = json.loads(
            self.order_ids
        )

        orders = pizza.by_status("Baked")
        order_ids_api = [order["id"] for order in orders]

        for _id in order_ids_parsed:
            if _id not in order_ids_api:
                return False

        return True
