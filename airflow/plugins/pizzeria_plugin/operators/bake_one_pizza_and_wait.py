import os
import json

import requests

from airflow.models.baseoperator import BaseOperator


class BakeOnePizzaAndWait(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        pizzeria_webserver_url = os.environ["PIZZERIA_WEBSERVER"]

        resp = requests.post(f"http://{pizzeria_webserver_url}/api/pizza/bake")

        if resp.status_code != 200:
            raise Exception(
                f"Something went wrong calling pizza api:\n{json.dumps(resp.json())}"
            )

        order_id = resp.json()["data"]["orderId"]

        return order_id
