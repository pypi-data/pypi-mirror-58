# -*- coding: utf-8 -*-

from .exec_env import ExecEnv
from ..runner import Runner
from ..config import StringBuilderConfig


class StringBuilder(ExecEnv):
    def __init__(self, config: StringBuilderConfig, variable: {}, runner: Runner):
        self.__config = config
        self.__default_var = variable
        self.__runner = runner

    def name(self):
        return 'string_builder'

    def var_assign(self, text: str, append_var=None):
        if append_var is None:
            append_var = {}

        if len(self.__default_var) + len(append_var) > 0:
            return text.format(**self.__default_var, **append_var)

        return text

    def build(self, command: str, work_dir=''):
        return self.__string_build(command, work_dir=work_dir)

    def up(self, command: str, work_dir=''):
        return self.__string_build(command, work_dir=work_dir)

    def down(self, command: str, work_dir=''):
        return self.__string_build(command, work_dir=work_dir)

    def run(self, command: str, work_dir=''):
        return self.__string_build(command, work_dir=work_dir)

    def __string_build(self, command: str, work_dir=''):
        if work_dir == '':
            work_dir = self.__runner.path_filter(self.var_assign(self.__config.working_dir))

        cmd = self.var_assign(command)
        cmd = self.var_assign(self.__config.run, {'command': cmd})

        return f'cd {work_dir} && {cmd}'
