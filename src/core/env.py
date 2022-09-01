from pathlib import Path

from envparse import Env as RawEnv, NOTSET


class Env:

    def __init__(self, path: str):
        self._path = Path(path)
        self._raw = RawEnv()
        self._read_envfile()

    def _read_envfile(self):
        path = self._path

        if not path.exists():
            raise FileNotFoundError(path)

        self._raw.read_envfile(path)

    def get(self, var_name: str, default=...) -> str:
        if default is ...:
            default = NOTSET

        return self._raw(var_name, default)


env = Env('.env')
