import os
import unittest
from src.environment import Environment


class EnvironmentTestCase(unittest.TestCase):
    def test_get_variable(self):
        environment = Environment({'a': 'b'})
        self.assertEqual('b', environment.get_variable('a'))
        self.assertEqual('', environment.get_variable('b'))
        os.environ['c'] = 'kek'
        self.assertEqual('kek', environment.get_variable('c'))

    def test_set_variable(self):
        environment = Environment()
        self.assertEqual('', environment.get_variable('a'))
        environment.set_variable('a', 'b')
        self.assertEqual('b', environment.get_variable('a'))
