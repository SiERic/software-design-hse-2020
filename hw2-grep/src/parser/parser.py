from typing import List

from src.parser.splitter import Splitter
from src.parser.expander import Expander
from src.environment import Environment


class Parser(object):
    """
    Class, preparing command line to interpreting
    Does all expansions, then split it into tokens
    """

    def __init__(self, environment: Environment):
        """
        Initializes the environment
        :param environment: environment with variables
        """
        self.environment = environment

    def parse(self, expression: str) -> List[List[str]]:
        """
        Parses command line into commands and tokens
        :param expression: expression to parse
        :return: list of commands, each command - list of tokens
        """
        expander = Expander(self.environment)
        splitter = Splitter()
        return splitter.split(expander.expand(expression))
