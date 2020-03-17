from abc import ABC, abstractmethod
from typing import List, Optional


class Command(ABC):
    """
    Basic abstract class for command
    """

    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens
        """
        self.args = args

    @abstractmethod
    def execute(self, stdin: Optional[str]) -> Optional[str]:
        """
        Executes command with given input
        :param stdin: command input
        """
