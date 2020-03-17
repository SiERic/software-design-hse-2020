import re

from src.environment import Environment
from src.parser.parse_utils import find_in_double_quotes


class Expander(object):
    """
    Class, performing all expansions on the command line
    Now only parameter expansion performed
    """
    def __init__(self, environment: Environment):
        """
        Initializes the environment
        :param environment: environment with variables
        """
        self.environment = environment

    def expand(self, expression: str) -> str:
        """
        Does all expansions
        :param expression: command line to do expansions on
        :return: expanded command line
        """
        return self._expand_variables(expression)

    def _expand_variables(self, expression: str) -> str:
        result = expression
        for index in find_in_double_quotes(expression, '$')[::-1]:
            name = ''
            i = index + 1
            while i < len(expression) and re.match(r'[a-z]|[A-Z]|[0-9]|_', expression[i]):
                name += expression[i]
                i += 1
            result = result[:index] + self.environment.get_variable(name) + result[index + len(name) + 1:]
        return result
