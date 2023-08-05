# -*- coding: utf-8 -*-

import unittest
from kumaoche.exec_env import Shell
from ..config import StubConfig
from ..runner import MocRunner


class TestShell(unittest.TestCase):
    def setUp(self):
        self.config = StubConfig.find('variable_assign_test_role').services[2]
        self.empty_config = StubConfig.find('empty_role').services[1]
        self.env = Shell(self.config.shell, self.config.environment, MocRunner)
        self.empty_env = Shell(self.empty_config.shell, self.empty_config.environment, MocRunner)
        self.src_text = 'git_host:{git_host},git_org:{git_org},git_repo:{git_repo}'
        self.dst_text = 'git_host:github.com,git_org:kumak1,git_repo:variable_assign_test_role'
        self.dst_empty_text = 'git_host:github.com,git_org:kumak1,git_repo:empty_role'

    def test_run(self):
        self.assertEqual(f"cd shell work_dir {self.dst_text} && shell run test_command", self.env.run("test_command"))
        self.assertEqual(f"cd shell work_dir {self.dst_text} && shell run {self.dst_text}", self.env.run(self.src_text))
        self.assertEqual("cd `ghq root` && shell run git_host:github.com,git_org:kumak1,git_repo:empty_role", self.empty_env.run(self.src_text))

    def test_var_assign(self):
        self.assertEqual(self.dst_text, self.env.var_assign(self.src_text))
        self.assertEqual('', self.env.var_assign(''))
        self.assertEqual('changed', self.env.var_assign('{var_test}', {'var_test': 'changed'}))
        self.assertEqual(self.dst_empty_text, self.empty_env.var_assign(self.src_text))


if __name__ == '__main__':
    unittest.main()
