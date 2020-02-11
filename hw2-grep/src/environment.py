import os
from typing import Dict


class Environment(object):
    """
    Environment, keeping assigned variables
    """
    def __init__(self, variables: Dict[str, str] = None):
        """
        Initializes environment with variables
        :param variables: dictionary of variables (name -> value)
        """
        if variables is None:
            variables = dict()
        self.variables: Dict[str, str] = variables

    def set_variable(self, name: str, value: str) -> None:
        """
        Sets value to variable
        :param name: variable name
        :param value: new value
        """
        self.variables[name] = value

    def get_variable(self, name: str) -> str:
        """
        Gets variable value by name
        If variable is not in the user dictionary, tries to get OS variable
        :param name: variable name
        :return: variable value
        """
        if self.variables.get(name) is not None:
            return self.variables.get(name)
        elif os.environ.get(name) is not None:
            return os.environ.get(name)
        else:
            return ''
