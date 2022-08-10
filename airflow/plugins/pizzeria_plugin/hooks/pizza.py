from typing import List, Dict
import os
import json

import requests

PIZZERIA_WEBSERVER_URL = os.environ["PIZZERIA_WEBSERVER"]


class PizzaApiException(Exception):
    pass


def bake() -> int:
    resp = requests.post(f"http://{PIZZERIA_WEBSERVER_URL}/api/pizza/bake")

    if resp.status_code != 200:
        raise PizzaApiException(
            "Something went wrong calling the pizza api:\n"
            f"{json.dumps(resp.json())}"
        )

    return resp.json()["data"]["orderId"]


def is_baked(order_id: int) -> bool:
    resp = requests.get(
        f"http://{PIZZERIA_WEBSERVER_URL}/api/pizza/is-baked/{order_id}"
    )

    if resp.status_code != 200:
        raise PizzaApiException(
            "Something went wrong calling the pizza api:\n"
            f"{json.dumps(resp.json())}"
        )

    return resp.json()["data"]["isBaked"]


def send_for_delivery(order_id: int) -> None:
    payload = {"orderId": order_id}

    resp = requests.post(
        f"http://{PIZZERIA_WEBSERVER_URL}/api/pizza/send-for-delivery",
        json=payload,
    )

    if resp.status_code != 200:
        raise PizzaApiException(
            "Something went wrong calling the pizza api:\n"
            f"{json.dumps(resp.json())}"
        )


def bake_batch() -> List[int]:
    resp = requests.post(f"http://{PIZZERIA_WEBSERVER_URL}/api/pizza/bake-batch")

    if resp.status_code != 200:
        raise PizzaApiException(
            "Something went wrong calling the pizza api:\n"
            f"{json.dumps(resp.json())}"
        )

    return resp.json()["data"]["orderIds"]


def by_status(order_status: str) -> List[Dict]:
    resp = requests.get(
        f"http://{PIZZERIA_WEBSERVER_URL}/api/pizza/by-status?orderStatus={order_status}"
    )

    if resp.status_code != 200:
        raise PizzaApiException(
            "Something went wrong calling the pizza api:\n"
            f"{json.dumps(resp.json())}"
        )

    return resp.json()["data"]
