import unittest

from src.executor import Executor
from src.environment import Environment


class ExecutorTestCase(unittest.TestCase):

    def test_execute_without_input(self):
        executor = Executor(Environment())
        self.assertEqual('\n', executor.execute([]))

    def test_execute_one_command(self):
        executor = Executor(Environment())
        self.assertEqual('kek\n', executor.execute([['echo', 'kek']]))

    def test_execute_two_commands(self):
        executor = Executor(Environment())
        self.assertEqual('    2    1    4\n', executor.execute([['echo', 'kek'], ['wc']]))

    def test_execute_two_commands_with_echo(self):
        executor = Executor(Environment())
        self.assertEqual('kek\n', executor.execute([['pwd'], ['echo', 'kek']]))

    def test_execute_empty_command(self):
        executor = Executor(Environment())
        self.assertEqual('\n', executor.execute([[]]))
        self.assertEqual('\n', executor.execute([['git', 'status'], []]))
