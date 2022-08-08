from airflow.models.baseoperator import BaseOperator


class BakeOnePizzaAndWait(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        message = "Hello world"
        print(message)
        return message
