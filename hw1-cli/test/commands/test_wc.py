import unittest
from src.commands.wc import Wc


class WcTestCase(unittest.TestCase):
    short_file_path = 'test/resources/short'
    long_file_path = 'test/resources/long'

    out_short = '    1    1    3 test/resources/short\n'
    out_long = '    3    3    15 test/resources/long\n'

    def test_short_stdin(self):
        wc = Wc([])
        stdin = 'kek'
        self.assertEqual('    1    1    3\n', wc.execute(stdin))

    def test_long_stdin(self):
        wc = Wc([])
        stdin = 'kek\nlol\narbidol'
        self.assertEqual('    3    3    15\n', wc.execute(stdin))

    def test_short_file(self):
        wc = Wc([self.short_file_path])
        self.assertEqual(self.out_short, wc.execute(None))

    def test_long_file(self):
        wc = Wc([self.long_file_path])
        self.assertEqual(self.out_long, wc.execute(None))

    def test_several_files(self):
        wc = Wc([self.short_file_path, self.long_file_path])
        self.assertEqual(self.out_short + self.out_long + '    4    4    18 total\n', wc.execute(None))

    def test_directory(self):
        directory_path = 'test/resources'
        wc = Wc([directory_path])
        self.assertEqual('wc: test/resources: Is a directory\n    0    0    0 test/resources\n', wc.execute(None))

    def test_file_not_exist(self):
        file_path = 'kek'
        wc = Wc([file_path])
        self.assertEqual('wc: kek: No such file or directory\n', wc.execute(None))
