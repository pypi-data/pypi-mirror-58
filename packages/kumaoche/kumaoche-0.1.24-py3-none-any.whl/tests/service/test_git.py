# -*- coding: utf-8 -*-

import unittest
from kumaoche.service import Git
from ..exec_env import MocEnv
from ..config import StubConfig


class TestGit(unittest.TestCase):
    def setUp(self):
        self.config = StubConfig.find('variable_assign_test_role')
        self.empty_config = StubConfig.find('empty_role')
        self.git = Git(MocEnv(self.config.environment), self.config.git)
        self.empty_git = Git(MocEnv(self.config.environment), self.empty_config.git)
        self.src_text = 'git_host:{git_host},git_org:{git_org},git_repo:{git_repo}'
        self.dst_text = 'git_host:github.com,git_org:kumak1,git_repo:variable_assign_test_role'

    def test_run(self):
        self.assertEqual(f"work_dir:repo {self.dst_text},command:git run test_command", self.git.run("test_command"))
        self.assertEqual(f"work_dir:repo {self.dst_text},command:git run {self.dst_text}", self.git.run(self.src_text))
        self.assertEqual(f"work_dir:repo {self.dst_text},command:git run {self.dst_text}", self.empty_git.run(self.src_text))

    def test_setup(self):
        self.assertEqual(f"work_dir:,command:git setup {self.dst_text}", self.git.setup())
        self.assertEqual(f"work_dir:,command:git setup {self.dst_text}", self.empty_git.setup())

    def test_update(self):
        self.assertEqual(f"work_dir:,command:git update {self.dst_text}", self.git.update())
        self.assertEqual(f"work_dir:,command:git update {self.dst_text}", self.empty_git.update())


if __name__ == '__main__':
    unittest.main()
