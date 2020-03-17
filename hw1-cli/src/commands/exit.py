from typing import List, Optional
from src.commands.command import Command
from src.exit_exception import ExitException


class Exit(Command):
    """
    Exit command
    Exits shell (raises ExitException)
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> None:
        """
        Executes 'exit' command
        :param stdin: command input (always ignored)
        """
        raise ExitException
