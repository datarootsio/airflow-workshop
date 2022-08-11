from datetime import timedelta
from typing import Tuple, Dict, Any
import random

import asyncio

from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.base import BaseTrigger, TriggerEvent


class RandomTrigger(BaseTrigger):
    def __init__(self, chance: float):
        super().__init__()
        self.chance = chance

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        return (
            "pizzeria_plugin.deferrable_operator.RandomTrigger",
            {"chance": self.chance},
        )

    async def run(self):
        sleep_time = 2

        rand = random.random()
        while self.chance < rand:
            print(f"chance({self.chance}): got rand {rand}")
            print(f"chance({self.chance}): sleeping {sleep_time}s")

            await asyncio.sleep(2)
            rand = random.random()

        print(f"chance({self.chance}): done")
        yield TriggerEvent(self.chance)


class RandomSensor(BaseSensorOperator):
    def __init__(self, chance: float, **kwargs):
        super().__init__(**kwargs)
        self.chance = chance

    def execute(self, context):
        self.defer(
            trigger=RandomTrigger(chance=self.chance),
            method_name="execute_complete",
        )

    def execute_complete(self, context, event=None):
        print("RandomSensor: yay i'm done")
        return
