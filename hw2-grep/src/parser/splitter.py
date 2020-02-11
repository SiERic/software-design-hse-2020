import re
from typing import List
from src.parser.parse_utils import clever_split, clean_from_quotes


class Splitter(object):
    """
    Class, that splits command line into commands and commands into tokens
    """

    @staticmethod
    def split(expression: str) -> List[List[str]]:
        """
        Splits given expressions into commands, each command - into tokens
        :param expression: expression to split
        :return: list of splitted commands
        """
        commands = clever_split(expression, re.compile(r'\|'))
        commands = list(map(lambda x: Splitter._split_command_into_tokens(x), commands))
        return commands

    @staticmethod
    def _split_command_into_tokens(command: str) -> List[str]:
        result = clever_split(command, re.compile(r'\s'))
        result = map(lambda x: clean_from_quotes(x), result)
        result = filter(lambda x: x != "", result)
        return list(result)
