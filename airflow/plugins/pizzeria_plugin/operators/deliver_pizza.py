from airflow.models.baseoperator import BaseOperator

from pizzeria_plugin.hooks import pizza


class DeliverPizza(BaseOperator):
    template_fields = ["order_id"]

    def __init__(self, order_id: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.order_id = order_id

    def execute(self, context):
        pizza.send_for_delivery(int(self.order_id))
