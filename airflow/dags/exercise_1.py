# Create a DAG that delivers a Pizza
# Schedule every hour, but not in the weekends
# You have 2 Operators available
#  - BakeOnePizzaAndWait
#  - DeliverPizza
# see:
#  - airflow/plugins/pizzeria_plugin/operators/bake_one_pizza_and_wait.py
#  - airflow/plugins/pizzeria_plugin/operators/deliver_pizza.py
# Put the python DAG file in ./dags folder
# Note: BakeOnePizzaAndWait fails if no pizza is ordered
# * extra points: recreate your DAG with the Taskflow API + the hooks in airflow/plugins/pizzeria_plugin/hooks/pizza.py