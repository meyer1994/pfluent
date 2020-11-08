import shlex
import subprocess
from subprocess import CompletedProcess, Popen, PIPE


class Runner(object):
    PIPE = PIPE

    def __init__(self, command: str):
        super(Runner, self).__init__()
        self._args = []
        self._env = None

        self.arg(command)

    def arg(self, *args: tuple) -> 'Runner':
        args = (str(a) for a in args)
        args = (shlex.quote(a) for a in args)
        self._args.extend(args)
        return self

    def env(self, **kwargs: dict) -> 'Runner':
        self._env = self._env or {}
        kwargs = {k: str(v) for k, v in kwargs.items()}
        self._env.update(kwargs)
        return self

    def run(self, *args: tuple, **kwargs: dict) -> CompletedProcess:
        return subprocess.run(self._args, env=self._env, *args, **kwargs)

    def popen(self, *args: tuple, **kwargs: dict) -> Popen:
        return subprocess.Popen(self._args, env=self._env, *args, **kwargs)
