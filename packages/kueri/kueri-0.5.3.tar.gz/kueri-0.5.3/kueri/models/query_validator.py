from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPICallError


class QueryValidator:

    def __init__(self, query, project_id):
        self.query = query
        self.project_id = project_id

    def validate_query(self):
        """
            Validate query
            :return: String valid query or not
        """
        client = bigquery.Client(project=self.project_id)
        job_config = bigquery.QueryJobConfig()
        job_config.use_query_cache = False
        job_config.use_legacy_sql = False
        job_config.dry_run = True
        try:
            client.query(
                query=self.query,
                location="US",
                job_config=job_config,
            )
        except GoogleAPICallError as google_exceptions:
            return "invalid query with value = {}".format(google_exceptions.errors[0].get('message'))
        return "valid query"
