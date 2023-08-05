import logging
import importlib
import sys
import os
import sqlparse
import json
import re


class DagBqQueryExtractor:
    
    def __init__(self, file_name, path_to_folder_file):
        self.file_name = file_name
        self.path_to_folder_file = path_to_folder_file
        self.bq_transformation_query = [
            {"name": "transformation_query", "type": "STRING"},
            {"name": "destination_table", "type": "STRING"}
        ]

    def read_dag_scripts(self):
        """
            Import module from python file
            :return: module python
        """

        dag_object = {}
        sys.path.append(os.path.abspath(self.path_to_folder_file))
        module_name = self.file_name[:-3]
        try:
            dag_object[module_name] = importlib.import_module(module_name)
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Module Not Found")
        return dag_object

    @staticmethod
    def filter_bigquery_operator_task(dag_object):
        """
            Create dictionary task and BigQueryOperator
            :param dag_object: Python Module
            :return: Dictionary
        """

        logging.info('Filtering valid BigQueryOperator tasks')
        bq_operator_dict = {}
        for module_name, module_content in dag_object.items():
            module_objects = module_content.__dict__
            for key, value in module_objects.items():
                if str(type(value)) == "<class 'airflow.contrib.operators.bigquery_operator.BigQueryOperator'>":
                    bq_operator_dict[key] = value
        return bq_operator_dict

    @staticmethod
    def retrieve_bigquery_operator_attribute(bq_operator_dict):
        """
            Retrieve sql from Dictionary bq_operator_dict
            :param bq_operator_dict: Dictionary of task name and it's BigQueryOperator
            :return: string
        """

        dict_task_query = {}
        logging.info('Retrieve BigQueryOperator attributes')
        for key, value in bq_operator_dict.items():
            if value.bql:
                query = value.bql
                query = query.replace('\n', '')
                query = re.sub(' +', ' ', query)
            else:
                query = value.sql
                query = '.'.join(query)
                query = re.sub(' +', ' ', query)
            dict_task_query[key] = query
        return json.dumps(dict_task_query)
