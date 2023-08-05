#!/usr/bin/python
import click
import coloredlogs
from kueri.commands.command_factory import CommandFactory


def parse_args(arguments):
    """
        Create dict of argument and value
        :return dictionary of payload
    """

    payload = {}
    for argument in arguments:
        argument = argument.split('=')
        key = argument[0]
        value = "=".join(argument[1:])
        payload[key] = value
    return payload


@click.command()
@click.argument('arguments', nargs=-1)
def main(arguments):
    """
        Execute the command
    """
    coloredlogs.install(fmt='%(levelname)s:%(message)s', level='INFO')
    payload = parse_args(arguments)
    command_string = payload.pop('cmd')
    command = CommandFactory(command_string).create(payload)
    command.execute()
