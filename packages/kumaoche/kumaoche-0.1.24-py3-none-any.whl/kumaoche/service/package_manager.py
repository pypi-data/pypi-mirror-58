# -*- coding: utf-8 -*-

from ..config import PackageManagerConfig
from ..exec_env import ExecEnv
from .service import Service


class PackageManager(Service):
    def __init__(self, env: ExecEnv, config: PackageManagerConfig):
        self.env = env
        self.__config = config

    def name(self):
        return self.__config.lang

    def run(self, command: str):
        var_command = {'command': self.env.var_assign(command)}
        return self.env.run(self.env.var_assign(self.__config.run, var_command))

    def setup(self):
        return self.env.run(self.env.var_assign(self.__config.setup))

    def update(self):
        return self.env.run(self.env.var_assign(self.__config.update))

    def test(self, suffix=''):
        cmd = self.env.var_assign(self.__config.test)

        if suffix != '':
            suffix = ' ' + self.env.var_assign(suffix)

        return self.env.run(f'{cmd}{suffix}')
