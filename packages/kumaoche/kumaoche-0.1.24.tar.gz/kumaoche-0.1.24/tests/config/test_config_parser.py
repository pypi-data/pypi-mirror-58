import unittest
import os

from kumaoche.config import ConfigParser


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.file_path_list = [os.path.dirname(__file__) + '/stub_config.yml']

    def test_all_roles(self):
        self.assertEqual(['variable_assign_test_role', 'empty_role'], ConfigParser.all_repository_names(self.file_path_list))

    def test_find(self):
        config = ConfigParser.find('variable_assign_test_role', self.file_path_list)
        self.assertEqual(config.services[0].lang, 'git')


if __name__ == '__main__':
    unittest.main()
