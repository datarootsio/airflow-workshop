from airflow.models.baseoperator import BaseOperator

from pizzeria_plugin.hooks import pizza


class BakePizzasInBatch(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        return pizza.bake_batch()
