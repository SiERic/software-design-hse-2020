import subprocess
from typing import List, Optional

from src.commands.command import Command


class External(Command):
    """
    External command
    Calls external command as subprocess
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens, first token should be command name
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> Optional[str]:
        """
        Executes command
        :param stdin: command input
        :return: command execution result
        """
        if len(self.args) == 0:
            return
        try:
            if stdin is None:
                proc = subprocess.run([self.args[0], *(self.args[1:])], stdout=subprocess.PIPE)
            else:
                proc = subprocess.run([self.args[0], *(self.args[1:])], stdout=subprocess.PIPE,
                                      input=stdin.encode('utf-8'))
        except FileNotFoundError:
            return self.args[0] + ': command not found\n'
        return proc.stdout.decode('utf-8')
