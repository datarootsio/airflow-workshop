from airflow.models.baseoperator import BaseOperator

from pizzeria_plugin.hooks import pizza


class OrderPizza(BaseOperator):
    template_fields = ["pizza_type"]

    def __init__(self, pizza_type: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pizza_type = pizza_type

    def execute(self, context):
        return pizza.order(self.pizza_type)
