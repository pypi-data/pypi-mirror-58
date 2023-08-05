# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ExecEnv(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def var_assign(self, text: str, append_var=None):
        raise NotImplementedError()

    @abstractmethod
    def build(self, command: str, work_dir=''):
        raise NotImplementedError()

    @abstractmethod
    def up(self, command: str, work_dir=''):
        raise NotImplementedError()

    @abstractmethod
    def down(self, command: str, work_dir=''):
        raise NotImplementedError()

    @abstractmethod
    def run(self, command: str, work_dir=''):
        raise NotImplementedError()
