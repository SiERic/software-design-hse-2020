import os
from typing import List, Tuple, Optional

from src.commands.command import Command


class Wc(Command):
    """
    Wc command
    Writes newline count, word count, and chars count of each file
    """
    def __init__(self, args: List[str]):
        """
        Initializes command with args
        :param args: list of tokens (files names)
        """
        super().__init__(args)

    def execute(self, stdin: Optional[str]) -> str:
        """
        Executes 'wc' command with given input
        :param stdin: command input
        :return: newline count, word count, and chars count of each file
        """
        if len(self.args) == 0 and stdin is not None:
            return self._get_formatted_statistics(*self._get_statistics(stdin))
        else:
            result = []
            total_lines = total_words = total_chars = 0
            for filename in self.args:
                if os.path.isfile(filename):
                    with open(filename, 'r') as fin:
                        lines, words, chars = self._get_statistics(fin.read())
                        result.append(self._get_formatted_statistics(lines, words, chars, filename))
                        total_lines += lines
                        total_words += words
                        total_chars += chars
                elif os.path.isdir(filename):
                    result += f'wc: {filename}: Is a directory\n' + self._get_formatted_statistics(0, 0, 0, filename)
                else:
                    result += f'wc: {filename}: No such file or directory\n'
            if len(self.args) > 1:
                result.append(self._get_formatted_statistics(total_lines, total_words, total_chars, 'total'))
            return ''.join(result)

    @staticmethod
    def _get_statistics(text: str) -> Tuple[int, int, int]:
        lines = text.count('\n') + 1
        words = len(text.split())
        chars = len(text)
        return lines, words, chars

    @staticmethod
    def _get_formatted_statistics(lines: int, words: int, chars: int, name: Optional[str] = None) -> str:
        if name is not None:
            return f'    {lines}    {words}    {chars} {name}\n'
        else:
            return f'    {lines}    {words}    {chars}\n'
