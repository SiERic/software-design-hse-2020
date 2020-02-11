import os
from typing import List, Optional

from src.commands.command import Command


class Cat(Command):
    """
    Cat command
    Reads and then writes file sequence
    """

    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'cat' command with given input
        :param stdin: command input, used then there're no arguments
        :return: concatenated content of the files
        """
        if len(self.args) == 0 and stdin is not None:
            return stdin
        result = ''
        for filename in self.args:
            if os.path.isfile(filename):
                with open(filename, 'r') as fin:
                    result += fin.read()
            elif os.path.isdir(filename):
                result += f'cat: {filename}: Is a directory\n'
            else:
                result += f'cat: {filename}: No such file or directory\n'
        return result
