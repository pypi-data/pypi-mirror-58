from airflow.models import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import datetime

DEFAULT_DATE = datetime(2015, 1, 1)
default_args = {'owner': 'de-team', 'start_date': DEFAULT_DATE}
DAG_NAME = 'test_retrieve_bigquery_param_bql'
dag = DAG(DAG_NAME, default_args=default_args)

test_retrieve_bigquery_param_bql = BigQueryOperator(
    task_id='test_retrieve_bigquery_param_bql',
    bql='select * from test_table',
    dag=dag,
    default_args=default_args,
    schema_update_options=None
)

