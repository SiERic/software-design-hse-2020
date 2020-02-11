import unittest

from termcolor import colored

from src.commands.grep import Grep


class GrepTestCase(unittest.TestCase):

    def test_no_match(self):
        grep = Grep(['kek'])
        self.assertEqual('', grep.execute('lol'))

    def test_exact_match(self):
        grep = Grep(['kek'])
        self.assertEqual(colored('kek', 'red') + '\n', grep.execute('kek'))

    def test_not_exact_match(self):
        grep = Grep(['kek'])
        self.assertEqual(colored('kek', 'red') + 'sik' + '\n', grep.execute('keksik'))

    def test_not_exact_match2(self):
        grep = Grep(['kek'])
        self.assertEqual('lol ' + colored('kek', 'red') + '\n', grep.execute('lol kek'))

    def test_exact_match_two_lines(self):
        grep = Grep(['kek'])
        self.assertEqual(2 * (colored('kek', 'red') + '\n'), grep.execute('kek\nkek'))

    def test_not_exact_match_two_lines(self):
        grep = Grep(['kek'])
        self.assertEqual(colored('kek', 'red') + 'sik' + '\n' + 'lol ' + colored('kek', 'red') + '\n',
                         grep.execute('keksik\nlol kek'))

    def test_match_twice(self):
        grep = Grep(['kek'])
        self.assertEqual(colored('kek', 'red') + ' ' + colored('kek', 'red') + '\n', grep.execute('kek kek'))

    def test_match_twice2(self):
        grep = Grep(['kek'])
        self.assertEqual(colored('kek', 'red') + 'ek' + '\n', grep.execute('kekek'))

    def test_match_word(self):
        grep = Grep(['-w', 'kek'])
        self.assertEqual(colored('kek', 'red') + '\n', grep.execute('kek'))

    def test_match_word2(self):
        grep = Grep(['-w', 'kek'])
        self.assertEqual('', grep.execute('keksik'))

    def test_match_word3(self):
        grep = Grep(['-w', 'kek'])
        self.assertEqual('lol ' + colored('kek', 'red') + '\n', grep.execute('lol kek'))

    def test_case_sensitive(self):
        grep = Grep(['kek'])
        self.assertEqual('', grep.execute('KeKsik'))

    def test_case_insensitive(self):
        grep = Grep(['-i', 'kek'])
        self.assertEqual(colored('KeK', 'red') + 'sik' + '\n', grep.execute('KeKsik'))

    def test_after_context(self):
        grep = Grep(['-A', '1', 'kek'])
        self.assertEqual(colored('kek', 'red') + '\n' + 'lol' + '\n', grep.execute('lol\nkek\nlol\narbidol'))

    def test_after_context_two_matches(self):
        grep = Grep(['-A', '1', 'kek'])
        self.assertEqual(colored('kek', 'red') + '\n' + 'lol' + '\n' + '--\n' + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute('lol\nkek\nlol\narbidol\nkeksik'))

    def test_after_context_two_matches_intersect(self):
        grep = Grep(['-A', '2', 'kek'])
        self.assertEqual(colored('kek', 'red') + '\n' + 'lol' + '\n' + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute('lol\nkek\nlol\nkeksik'))

    def test_file(self):
        kek_path = 'test/resources/kek'
        grep = Grep(['kek', kek_path])
        self.assertEqual(colored(kek_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n',
                         grep.execute(None))

    def test_big_file(self):
        keksik_path = 'test/resources/keksik'
        grep = Grep(['kek', keksik_path])
        self.assertEqual(colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute(None))

    def test_big_file_after_context(self):
        keksik_path = 'test/resources/keksik'
        grep = Grep(['-A', '1', 'kek', keksik_path])
        self.assertEqual(colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         colored(keksik_path, 'magenta') + colored('-', 'cyan') + 'lol' + '\n' +
                         '--' + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute(None))

    def test_two_files(self):
        kek_path = 'test/resources/kek'
        keksik_path = 'test/resources/keksik'
        grep = Grep(['kek', kek_path, keksik_path])
        self.assertEqual(colored(kek_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute(None))

    def test_two_files_after_context(self):
        kek_path = 'test/resources/kek'
        keksik_path = 'test/resources/keksik'
        grep = Grep(['-A', '1', 'kek', kek_path, keksik_path])
        self.assertEqual(colored(kek_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         '--' + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + '\n' +
                         colored(keksik_path, 'magenta') + colored('-', 'cyan') + 'lol' + '\n' +
                         '--' + '\n' +
                         colored(keksik_path, 'magenta') + colored(':', 'cyan') + colored('kek', 'red') + 'sik' + '\n',
                         grep.execute(None))

    def test_error(self):
        grep = Grep(['-z', 'kek'])
        self.assertEqual('usage: grep [-i] [-w] [-A NUM] pattern [file [file ...]]\ngrep: unrecognized arguments: -z\n',
                         grep.execute('kekek'))
