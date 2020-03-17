import unittest
from src.commands.pwd import Pwd


class PwdTestCase(unittest.TestCase):
    directory_path = 'hw1-cli\n'

    def test_without_args_without_stdin(self):
        pwd = Pwd([])
        self.assertEqual(self.directory_path, pwd.execute(None)[-len(self.directory_path):])

    def test_with_args_with_stdin(self):
        pwd = Pwd(['kek', 'lol'])
        self.assertEqual(self.directory_path, pwd.execute('kek')[-len(self.directory_path):])

    def test_with_args_without_stdin(self):
        pwd = Pwd(['kek', 'lol'])
        self.assertEqual(self.directory_path, pwd.execute(None)[-len(self.directory_path):])

    def test_without_args_with_stdin(self):
        pwd = Pwd([])
        self.assertEqual(self.directory_path, pwd.execute('kek')[-len(self.directory_path):])
