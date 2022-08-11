from airflow.models import DagBag


def test_no_import_errors():
    dag_bag = DagBag(dag_folder="/workspace/airflow-workshop/airflow/dags")
    assert len(dag_bag.import_errors) == 0


def test_validate_dag_id_doesnt_use_underscore():
    dag_bag = DagBag(dag_folder="/workspace/airflow-workshop/airflow/dags")
    for dag_id, dag in dag_bag.dags.items():
        assert "_" not in dag_id
