import os
from typing import List, Optional
from src.commands.command import Command


class Pwd(Command):
    """
    Pwd command
    Writes the full pathname of the current working directory
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens (ignored)
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'pwd' command with given input (input is always ignored)
        :param stdin: command input
        :return: full pathname of the current working directory
        """
        return os.getcwd() + '\n'
