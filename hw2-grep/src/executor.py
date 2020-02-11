import re
from typing import List, Optional

from src.commands.cat import Cat
from src.commands.echo import Echo
from src.commands.exit import Exit
from src.commands.external import External
from src.commands.grep import Grep
from src.commands.pwd import Pwd
from src.commands.wc import Wc
from src.environment import Environment


class Executor(object):
    """
    Executes commands chain
    """
    ASSIGNMENT_PATTERN = r'[a-zA-Z]+?=\w*'

    COMMANDS = {'cat': Cat,
                'echo': Echo,
                'exit': Exit,
                'grep': Grep,
                'pwd': Pwd,
                'wc': Wc}

    def __init__(self, environment: Environment):
        """
        Initializes the environment
        :param environment: environment with variables
        """
        self.environment = environment

    def execute(self, commands: List[List[str]]) -> str:
        """
        Executes pipeline of commands
        Each command output is a string, which used as next command input
        :param commands: list of commands (each command is a list of tokens)
        :return: result of last command execution
        """
        if len(commands) == 1 and len(commands[0]) == 1 and re.match(self.ASSIGNMENT_PATTERN, commands[0][0]):
            name, value = commands[0][0].split('=')
            self.environment.set_variable(name, value)
            return '\n'

        stdin = None
        for command in commands:
            stdin = self._call_command(command, stdin)
        if stdin is not None:
            return stdin
        else:
            return '\n'

    def _call_command(self, command: List[str], stdin: str) -> Optional[str]:
        if command[0] in self.COMMANDS.keys():
            builtin = self.COMMANDS[command[0]](command[1:])
            new_stdin = builtin.execute(stdin)
        else:
            external = External(command)
            new_stdin = external.execute(stdin)
        return new_stdin
