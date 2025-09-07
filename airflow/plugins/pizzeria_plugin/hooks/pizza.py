import time
import random

def bake_pizza() -> int:
    print("Started baking a pizza.")

    for i in range(5):
        print(f"Baking... [{i}/5]")
        time.sleep(1)

    order_id = random.randint(1, 1_000_000)
    print(f"Pizza is ready. Order id: {order_id}")
    return order_id

def deliver_pizza(order_id: int) -> None:
    print(f"Delivered pizza with order ID: {order_id}!")