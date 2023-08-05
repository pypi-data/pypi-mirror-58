from dataclasses import dataclass
from typing import Callable
import subprocess
import logging

logger = logging.getLogger(__name__)


class Task:
    def __init__(self): ...

    def __call__(self, *args, **kwargs): ...


def cmd_command(command: str, *args):
    subprocess.run([command] + list(args), shell=True, check=True)


@dataclass
class Executor:
    callback: Callable = None
    args: list = None
    kwargs: list = None
    known_exceptions: list = None

    @property
    def knowledge_errors(self) -> list:
        return self.known_exceptions or []

    def on_error(self, exception):
        logger.exception(f'{self}. {exception}')

    def on_success(self):
        logger.exception(f'{self} Task {self.callback.__name__} successful performed')

    def run(self):
        _task = self.callback
        t_args = self.args or []
        t_kwargs = self.kwargs or {}
        try:
            _task(*t_args, **t_kwargs)
        except Exception as e:
            if e in self.knowledge_errors:
                self.on_error(e)

    def __str__(self):
        return f'"{type(self).__name__}". {self.__doc__}.'

