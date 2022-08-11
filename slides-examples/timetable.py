import AirflowPlugin
import Optional
import DateTime
import Dict
import Any
from airflow.timetables.base import DagRunInfo, DataInterval, TimeRestriction, Timetable


class MyTimetable(Timetable):
    @classmethod
    def deserialize(cls, data: Dict[str, Any]) -> Timetable:
        ...

    def serialize(self) -> Dict[str, Any]:
        return {}


    def infer_manual_data_interval(self, run_after: DateTime) -> DataInterval:
        ...

    def next_dagrun_info(
        self,
        *,
        last_automated_data_interval: Optional[DataInterval],
        restriction: TimeRestriction,
    ) -> Optional[DagRunInfo]:
        ...
        return DagRunInfo.interval(start=..., end=...)

class MyPlugin(AirflowPlugin):
    name = "my_plugin"
    timetables = [MyTimetable]


import dagfactory

my_dags = dagfactory.DagFactory(
    "/path/to/yamls"
)

from datetime import timedelta

from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.temporal import TimeDeltaTrigger


class WaitOneHourSensor(BaseSensorOperator):
    def execute(self, context):
        self.defer(
            trigger=TimeDeltaTrigger(timedelta(hours=1)), 
            method_name="execute_complete"
        )

    def execute_complete(self, context, event=None):
        # We have no more work to do here. Mark as complete.
        return

import MyOperator, DAG, DEFAULT_DATE, TaskInstance, datetime




def test_my_operator():
    dag = DAG("test_dag", start_date=DEFAULT_DATE)

    task = MyOperator(my_operator_param="hey", task_id="my_op", dag=dag)
    ti = TaskInstance(task=task, execution_date=datetime.now())
    result = task.execute(ti.get_template_context())

    assert result is True