from airflow.models import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import datetime

DEFAULT_DATE = datetime(2015, 1, 1)
default_args = {'owner': 'de-team', 'start_date': DEFAULT_DATE}
DAG_NAME = 'test_read_dag_scripts'
dag = DAG(DAG_NAME, default_args=default_args)

test_read_dag_scripts = BigQueryOperator(
    task_id='test_read_dag_scripts',
    bql='select * from test_table',
    dag=dag,
    default_args=default_args,
    schema_update_options=None
)
