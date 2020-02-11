import argparse
import os
import re
from typing import List, Optional

from termcolor import colored

from src.commands.command import Command


class Grep(Command):
    """
    Grep command
    Searches with the regular expression and prints all matching lines
    Supports flags:
    -i, --ignore-case
              Ignore case distinctions in  both  the  PATTERN  and  the  input
              files.
    -w, --word-regexp
              Select only those  lines  containing  matches  that  form  whole
              words.
    -A NUM, --after-context=NUM
              Print NUM  lines  of  trailing  context  after  matching  lines.
              Places   a  line  containing  a  group  separator  (--)  between
              contiguous groups of matches.
    """

    def __init__(self, args: List[str]):
        """
        Initializes command with args
        Also parses command arguments
        :param args: list of tokens
        """
        super().__init__(args)
        self._parse_arguments()

    def execute(self, stdin: Optional[str]) -> str:
        """
         Executes 'grep' command with given input
        :param stdin: command input, used then there're no files in arguments
        :return: lines containing pattern
        """

        if self.exception is not None:
            return str(self.exception)
        if len(self.files) == 0 and stdin is not None:
            return self._match(stdin)
        result = ''
        for filename in self.files:
            if os.path.isfile(filename):
                with open(filename, 'r') as fin:
                    ans = self._match(fin.read(), filename)
                    if self.after_context is not None and result != '' and ans != '':
                        result += '--\n'
                    result += ans
            elif os.path.isdir(filename):
                result += f'grep: {filename}: Is a directory\n'
            else:
                result += f'grep: {filename}: No such file or directory\n'
        return result

    def _match(self, data: str, filename: Optional[str] = None) -> str:
        lines = data.split('\n')
        matched_lines = []
        for (i, line) in enumerate(lines):
            if self.pattern.search(line):
                matched_lines.append(i)
        last_matched = -1
        result = ''
        for i in matched_lines:
            if last_matched != -1 and last_matched < i and self.after_context is not None:
                result += '--\n'
            to = min(len(lines) - 1, i + self.after_context) if self.after_context is not None else i
            for j in range(max(last_matched + 1, i), to + 1):
                result += self._match_line(lines[j], filename)
            last_matched = to
        return result

    def _match_line(self, line: str, filename: Optional[str]) -> str:
        matches = [(i.start(), i.end()) for i in self.pattern.finditer(line)]
        if len(matches) == 0:
            if filename is not None:
                return colored(filename, 'magenta') + colored('-', 'cyan') + line + '\n'
            else:
                return line + '\n'
        else:
            last_index = -1
            if filename is not None:
                result = colored(filename, 'magenta') + colored(':', 'cyan')
            else:
                result = ''
            for (start, end) in matches:
                if last_index < start:
                    result += line[last_index + 1:start]
                result += colored(line[max(start, last_index + 1): end], 'red')
                last_index = end - 1
            result += line[last_index + 1::]
            return result + '\n'

    def _parse_arguments(self):
        parser = _ArgumentParser(prog='grep', add_help=False)
        parser.add_argument('-i', '--ignore-case', action='store_true',
                            help='Ignore case distinctions in both the pattern and the input files')
        parser.add_argument('-w', '--word-regexp', action='store_true',
                            help='Select only those lines containing matches that form whole words')
        parser.add_argument('-A', '--after-context', metavar='NUM', type=int, default=None,
                            help='Print NUM lines of trailing context after matching lines')

        parser.add_argument('pattern', type=str)
        parser.add_argument('file', nargs='*')

        self.exception = None

        try:
            conf = parser.parse_args(self.args)

            self.files = conf.file
            self.after_context = conf.after_context
            pattern = conf.pattern
            if conf.word_regexp:
                pattern = r'\b' + pattern + r'\b'
            if conf.ignore_case:
                self.pattern = re.compile(pattern, re.IGNORECASE)
            else:
                self.pattern = re.compile(pattern)
        except Exception as e:
            self.exception = e


class _ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        message = f'{self.format_usage()}{self.prog}: {message}\n'
        raise Exception(message)

