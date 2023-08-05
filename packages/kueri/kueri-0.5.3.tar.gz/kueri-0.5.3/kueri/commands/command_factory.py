import importlib
import sys
import logging


class CommandFactory:

    CLASS_SUFFIX = 'Command'
    FILE_SUFFIX = '_command'
    BASE_MODULE = 'kueri.commands'

    def __init__(self, command_string):
        self.command_string = command_string
        self.command_class = self._import_class()

    def _class_name(self):
        """
            Parsing name module in to camelcase then join with const FILE_SUFFIX
            :return: Class name of module
        """

        command_string_camelcase = ''.join(x.title() for x in self.command_string.split('_'))
        return command_string_camelcase + self.CLASS_SUFFIX

    def _import_class(self):
        """
            Import class and assign attribute of the class based on input
            :return: Object of class
        """

        try:
            mod = importlib.import_module('{}.{}{}'.format(self.BASE_MODULE, self.command_string, self.FILE_SUFFIX))
            cls = getattr(mod, self._class_name())
        except ModuleNotFoundError:
            logging.info('Invalid Command')
            sys.exit(1)
        except AttributeError:
            raise AttributeError
            logging.info('Incorrect command class name. Contact DE Team')
            sys.exit(1)
        return cls

    def create(self, payload):
        """
            Crate object of class
            :param payload: Input parameter as attribute of class
            :return:
        """

        return self.command_class(payload)
