from kueri.models.query_validator import QueryValidator
from .base_command import BaseCommand
import logging


class QueryValidatorCommand(BaseCommand):

    def execute(self):
        """
            Main to execute QueryValidator
        """

        query_validator = QueryValidator(**self.payload)
        result = query_validator.validate_query()
        print("result = {}".format(result))
        return result
