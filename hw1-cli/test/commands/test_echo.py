import unittest
from src.commands.echo import Echo


class EchoTestCase(unittest.TestCase):

    def test_empty(self):
        echo = Echo([])
        self.assertEqual('\n', echo.execute(None))

    def test_empty_with_stdin(self):
        echo = Echo([])
        self.assertEqual('\n', echo.execute('kek'))

    def test_with_arguments(self):
        echo = Echo(['1', '2', '3'])
        self.assertEqual('1 2 3\n', echo.execute(None))

    def test_with_arguments_with_stdin(self):
        echo = Echo(['1', '2', '3'])
        self.assertEqual('1 2 3\n', echo.execute('kek'))

    def test_with_strange_arguments(self):
        echo = Echo(['kek', '\"\'', '   !!!  '])
        self.assertEqual('kek \"\'    !!!  \n', echo.execute(None))

