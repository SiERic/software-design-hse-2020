"""
Module with some useful parsing functions
"""

import re
from typing import List, Pattern


def find_in_double_quotes(text: str, symbol: str) -> List[int]:
    """
    Finds all occurrences of the symbol in the given text
    :param text: text to find symbol in
    :param symbol: symbol to look for
    :return: list of symbol occurrences in the given text
    """
    quotes_state = QuotesState(False, False)
    indices = []
    for (index, character) in enumerate(text):
        quotes_state.change_state(character)
        if character == symbol and not quotes_state.in_single_quotes:
            indices.append(index)
    return indices


def clever_split(text: str, pattern: Pattern[str]) -> List[str]:
    """
    Splits given text by the symbols, which are not in quotes
    :param text: text to split
    :param pattern: pattern to split by
    :return: splitted text
    """
    quotes_state = QuotesState(False, False)
    indices = []
    for (index, character) in enumerate(text):
        quotes_state.change_state(character)
        if re.match(pattern, character) is not None and \
                not (quotes_state.in_single_quotes or quotes_state.in_double_quotes):
            indices.append(index)
    result = []
    indices = [-1] + indices + [len(text)]
    for i in range(len(indices) - 1):
        result.append(text[indices[i] + 1:indices[i + 1]])
    return result


def clean_from_quotes(word: str) -> str:
    """
    Removes unescaped occurrences of ' and "
    :param word: word to clean from quotes
    :return: clean word
    """
    quotes_state = QuotesState(False, False)
    result = ''
    for (index, character) in enumerate(word):
        if (character == '\"' or character == '\'') and quotes_state.change_state(character):
            pass
        else:
            result += character
    return result


class QuotesState(object):
    """
    Stores quotes state
    """

    def __init__(self, in_single_quotes: bool, in_double_quotes: bool):
        """
        Initializes state
        :param in_single_quotes: is cursor in single quotes
        :param in_double_quotes: is cursor in double quotes
        """
        self.in_double_quotes = in_double_quotes
        self.in_single_quotes = in_single_quotes

    def change_state(self, character: str) -> bool:
        """
        Changes state with current character
        :param character: current character
        :return: if the state changes
        """
        if character == '\"' and not self.in_single_quotes:
            self.in_double_quotes = not self.in_double_quotes
            return True
        elif character == '\'' and not self.in_double_quotes:
            self.in_single_quotes = not self.in_single_quotes
            return True
        return False
