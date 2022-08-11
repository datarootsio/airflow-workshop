from airflow.sensors.base_sensor_operator import BaseSensorOperator

from pizzeria_plugin.hooks import pizza


class WaitForAPizzaToBeDelivered(BaseSensorOperator):
    template_fields = ["order_id"]

    def __init__(self, order_id: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.order_id = order_id

    def poke(self, context):
        orders = pizza.by_status("Delivered")
        order_ids_api = [order["id"] for order in orders]

        return int(self.order_id) in order_ids_api
