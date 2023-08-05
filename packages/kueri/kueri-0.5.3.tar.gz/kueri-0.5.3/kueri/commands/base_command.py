import abc


class BaseCommand(abc.ABC):

    def __init__(self, payload):
        self.payload = payload

    @abc.abstractmethod
    def execute(self):
        """
            Abstract Method to execute models
        """
        pass
