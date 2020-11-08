from unittest import TestCase
from unittest.mock import patch

from pfluid import Runner


class TestRunner(TestCase):
    def test_init(self):
        """ Adds command to args """
        runner = Runner('ls')
        self.assertListEqual(runner._args, ['ls'])

    def test_arg(self):
        """ Adds arguments to args list """
        runner = Runner('ls')\
            .arg('-h')\
            .arg('-l')
        self.assertListEqual(runner._args, ['ls', '-h', '-l'])

    def test_env(self):
        """ Adds kwargs to environment """
        runner = Runner('ls')\
            .env(KEY='key')
        self.assertDictEqual(runner._env, {'KEY': 'key'})

    @patch('pfluid.subprocess.run')
    def test_run(self, run):
        """ Runs process """
        runner = Runner('ls').run(check=True)
        run.assert_called_once_with(['ls'], env=None, check=True)

    @patch('pfluid.subprocess.Popen')
    def test_open(self, Popen):
        """ Opens process """
        runner = Runner('ls').popen(bufsize=0)
        Popen.assert_called_once_with(['ls'], env=None, bufsize=0)
