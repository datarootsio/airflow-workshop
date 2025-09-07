from airflow.models.baseoperator import BaseOperator

from pizzeria_plugin.hooks import pizza


class BakeOnePizzaAndWait(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context) -> int:
        return pizza.bake_pizza()
