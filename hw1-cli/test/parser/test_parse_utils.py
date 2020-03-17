import unittest
from src.parser.parse_utils import *


class ParseUtilsTestCase(unittest.TestCase):
    def test_quotes_state(self):
        quotes_state = QuotesState(False, False)
        quotes_state.change_state('\'')
        self.assertEqual(quotes_state.in_single_quotes, True)
        self.assertEqual(quotes_state.in_double_quotes, False)

    def test_find_in_double_quotes(self):
        self.assertEqual([0], find_in_double_quotes('$ \'$\'', '$'))
        self.assertEqual([0, 3], find_in_double_quotes('$ \"$\"', '$'))
        self.assertEqual([0], find_in_double_quotes('$', '$'))
        self.assertEqual([0, 3], find_in_double_quotes('$a $b', '$'))
        self.assertEqual([0, 2], find_in_double_quotes('$a$b', '$'))

    def test_clever_split(self):
        self.assertEqual(['123', ' a'], clever_split('123| a', re.compile(r'\|')))
        self.assertEqual(['123', ' a \"12 | 23\"'], clever_split('123| a \"12 | 23\"', re.compile(r'\|')))

    def test_from_quotes(self):
        self.assertEqual('kek', clean_from_quotes('\"kek\"'))
        self.assertEqual('\'kek\'', clean_from_quotes('\"\'kek\'\"'))
        self.assertEqual('\"kek\"', clean_from_quotes('\'\"kek\"\''))


if __name__ == '__main__':
    unittest.main()
