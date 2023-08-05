# -*- coding: utf-8 -*-

from ..config import GitConfig
from ..exec_env import ExecEnv
from .service import Service


class Git(Service):
    def __init__(self, env: ExecEnv, config: GitConfig):
        self.env = env
        self.__config = config

    def name(self):
        return 'git'

    def run(self, command: str):
        repo_dir = self.env.var_assign(self.__config.repo_dir)
        var_command = {'command': self.env.var_assign(command)}

        return self.env.run(self.env.var_assign(self.__config.run, var_command), work_dir=repo_dir)

    def setup(self):
        return self.env.run(self.env.var_assign(self.__config.setup))

    def update(self):
        return self.env.run(self.env.var_assign(self.__config.update))
