from abc import ABC, abstractmethod
from typing import List, Optional


class Command(ABC):

    def __init__(self, args: List[str]):
        self.args = args

    @abstractmethod
    def execute(self, stdin: str) -> Optional[str]:
        pass
