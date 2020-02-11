import unittest
from src.parser.splitter import Splitter


class SplitterTestCase(unittest.TestCase):
    def test_split_command_into_tokens(self):
        splitter = Splitter()
        self.assertEqual(['a', 'b', 'c'], splitter._split_command_into_tokens('a b c'))
        self.assertEqual(['a', 'b', 'kek lol'], splitter._split_command_into_tokens('a b \"kek lol\"'))

    def test_split(self):
        splitter = Splitter()
        self.assertEqual([['a', 'b', 'c'], ['d', 'e', 'f']], splitter.split("a b c | d e f"))
        self.assertEqual([['a', 'b | b', 'c'], ['d', 'e', 'f']], splitter.split("a \"b | b\" c | \"d\" e f"))
