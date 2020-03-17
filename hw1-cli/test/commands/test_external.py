import unittest
from src.commands.external import External


class ExternalTestCase(unittest.TestCase):
    def test_cat_with_file(self):
        short_file_path = 'test/resources/short'
        external = External(['cat', short_file_path])
        stdin = open(short_file_path, 'r').read()
        self.assertEqual(stdin, external.execute(None))

    def test_cat_with_stdin(self):
        external = External(['git'])
        self.assertTrue(external.execute('help').find('commit') >= 0)

    def test_command_not_exist(self):
        external = External(['keksiki'])
        self.assertEqual('keksiki: command not found\n', external.execute(None))

