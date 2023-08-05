# -*- coding: utf-8 -*-

import unittest
from kumaoche.service import PackageManager
from ..exec_env import MocEnv
from ..config import StubConfig


class TestPackageManager(unittest.TestCase):
    def setUp(self):
        self.config = StubConfig.find('variable_assign_test_role').services[1]
        self.empty_config = StubConfig.find('empty_role').services[1]
        self.pm = PackageManager(MocEnv(self.config.environment), self.config)
        self.empty_pm = PackageManager(MocEnv(self.config.environment), self.empty_config)
        self.src_text = 'git_host:{git_host},git_org:{git_org},git_repo:{git_repo}'
        self.dst_text = 'git_host:github.com,git_org:kumak1,git_repo:variable_assign_test_role'

    def test_run(self):
        self.assertEqual(f"work_dir:,command:pm run test_command", self.pm.run("test_command"))
        self.assertEqual(f"work_dir:,command:pm run {self.dst_text}", self.pm.run(self.src_text))
        self.assertEqual(f"work_dir:,command:", self.empty_pm.run(self.src_text))

    def test_setup(self):
        self.assertEqual(f"work_dir:,command:pm setup {self.dst_text}", self.pm.setup())
        self.assertEqual(f"work_dir:,command:", self.empty_pm.setup())

    def test_update(self):
        self.assertEqual(f"work_dir:,command:pm update {self.dst_text}", self.pm.update())
        self.assertEqual(f"work_dir:,command:", self.empty_pm.update())

    def test_test(self):
        self.assertEqual(f"work_dir:,command:pm test {self.dst_text}", self.pm.test())
        self.assertEqual(f"work_dir:,command:pm test {self.dst_text} {self.dst_text}", self.pm.test(self.src_text))


if __name__ == '__main__':
    unittest.main()
