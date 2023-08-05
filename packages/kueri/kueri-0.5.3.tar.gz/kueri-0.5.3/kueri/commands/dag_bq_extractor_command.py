from kueri.models.dag_bq_query_extractor import DagBqQueryExtractor
from .base_command import BaseCommand
import logging


class DagBqExtractorCommand(BaseCommand):

    def execute(self):
        """
            Main to execute DAGBqQueryExtractor
        """

        dag_bq_extractor = DagBqQueryExtractor(**self.payload)
        try:
            dag_object = dag_bq_extractor.read_dag_scripts()
            bq_operator_dict = dag_bq_extractor.filter_bigquery_operator_task(dag_object)
            query = dag_bq_extractor.retrieve_bigquery_operator_attribute(bq_operator_dict)
            print(query)
        except Exception as e:
            raise e
        return query
