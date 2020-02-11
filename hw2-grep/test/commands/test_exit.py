import unittest
from src.commands.exit import Exit


class ExitTestCase(unittest.TestCase):
    def test_without_args(self):
        exit_command = Exit([])
        self.assertRaises(SystemExit, lambda: exit_command.execute(None))

    def test_with_args(self):
        exit_command = Exit(['kek', 'lol'])
        self.assertRaises(SystemExit, lambda: exit_command.execute(None))

    def test_without_args_with_stdin(self):
        exit_command = Exit([])
        self.assertRaises(SystemExit, lambda: exit_command.execute('kek'))

    def test_with_args_with_stdin(self):
        exit_command = Exit(['kek', 'lol'])
        self.assertRaises(SystemExit, lambda: exit_command.execute('kek'))
