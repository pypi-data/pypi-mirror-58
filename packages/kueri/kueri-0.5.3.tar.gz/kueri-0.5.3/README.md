# kueri

A query toolkit

## Description

There are two module in kueri package:

1. Query extractor from DAG file : Used for extract query from each task in a dag file
2. Query validator : Validate query using dry run api bigquery. This module use **standard sql dialect**

## How to run unit test

### Need to install berfore run unit test

- pytest (pip install pytest)
- pytest-cov (pip install pytest-cov)
- rootpath (pip install rootpath)
- mock
- sqlparse
- rootpath
- apache-airflow[gcp]==1.10.5
- requests

### Command to run unit test

- pytest (output only pass or failed testing)
- pytest --cov-report term --cov=kueri tests/  (Give percentage coverage of unit testing)
- pytest --cov-report term-missing --cov=kueri tests/ (give line of code function that not covered in unit test)

## Installation

``` shell
pip3 install kueri
```

**Note**\
***Before you install kueri, please make sure that you have installed all module that's your dag need***

## Usage

### Query validator

``` shell
kueri cmd='query_validator' query='{query need to validate}' project_id='{project id of your query}'
```

example:

``` shell
kueri cmd='query_validator' query='select * from `mapan-data-prd.mapan_data_prod_dv.hub_arisan_chairmen`' project_id='mapan-data-prd'
```

### Query extractor from DAG file

``` shell
kueri cmd="dag_bq_extractor" path_to_folder_file='{path to folder folder file DAG}' file_name='{name of file}'
```

example:

``` shell
kueri cmd="dag_bq_extractor" path_to_folder_file='/Users/mapan_1004/Documents/workspace/list_of_dag/' file_name='test_retrieve_bigquery_param_bql_dag.py'
```

**Note**\
***Please use `'` (single quote) instead of `"` (double quotes) in parameter.***
