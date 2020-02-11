import unittest
from src.parser.expander import Expander
from src.environment import Environment


class ExpanderTestCase(unittest.TestCase):
    def test_expand_variables(self):
        expander = Expander(Environment({'a': 'kek', 'b': '42'}))
        self.assertEqual('kek', expander._expand_variables('$a'))
        self.assertEqual('\"kek\"', expander._expand_variables('\"$a\"'))
