from typing import List, Optional
from src.commands.command import Command


class Echo(Command):
    """
    Echo command
    Writes its arguments separated by spaces
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'echo' command with given input (input is always ignored)
        :param stdin: command input
        :return: command arguments separated by spaces
        """
        return ' '.join(self.args) + '\n'
