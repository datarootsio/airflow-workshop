



from airflow.models.baseoperator import BaseOperator


class MyOperator(BaseOperator):
    template_fields = ...

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        ...

    def execute(self, context):
        ...

        return ...



from airflow.sensors.base_sensor_operator import BaseSensorOperator


class MySensor(BaseSensorOperator):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        ...
    
    def poke(self, context):
        if ...:
            return False
        
        return True

