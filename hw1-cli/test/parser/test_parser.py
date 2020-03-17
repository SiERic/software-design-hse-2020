import unittest
from src.parser.parser import Parser
from src.environment import Environment


class ParserTestCase(unittest.TestCase):
    def test_parse(self):
        parser = Parser(Environment({'a': 'b'}))
        self.assertEqual([['a', 'b', 'c'], ['d', 'e', 'f']], parser.parse("a b c | d e f"))
        self.assertEqual([['a', 'b | b', 'c'], ['d', 'e', 'f']], parser.parse("a \"b | b\" c | \"d\" e f"))
        self.assertEqual([['a', 'b | b', 'c'], ['d', 'e', 'b', 'b']], parser.parse("a \"b | b\" c | \"d\" e $a \"$a\""))
