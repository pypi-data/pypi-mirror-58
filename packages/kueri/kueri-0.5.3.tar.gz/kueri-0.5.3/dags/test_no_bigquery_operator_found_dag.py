from airflow.models import DAG
from datetime import datetime

DEFAULT_DATE = datetime(2015, 1, 1)
default_args = {'owner': 'de-team', 'start_date': DEFAULT_DATE}
DAG_NAME = 'test_no_bigquery_operators_found'
dag = DAG(DAG_NAME, default_args=default_args)
