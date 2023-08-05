import unittest
from kumaoche.config import GitConfig


class TestGitConfig(unittest.TestCase):
    def test_init(self):
        parsed_yaml = {
            'git': {
                'run': '0',
                'setup': '1',
                'update': '2',
                'repo_dir': '3',
            }
        }
        config = GitConfig(parsed_yaml)
        self.assertEqual('git', config.lang)
        self.assertEqual('shell', config.env)
        self.assertEqual('0', config.run)
        self.assertEqual('1', config.setup)
        self.assertEqual('2', config.update)
        self.assertEqual('3', config.repo_dir)

        config = GitConfig({})
        self.assertEqual('git', config.lang)
        self.assertEqual('shell', config.env)
        self.assertEqual('', config.run)
        self.assertEqual('', config.setup)
        self.assertEqual('', config.update)
        self.assertEqual('', config.repo_dir)



if __name__ == '__main__':
    unittest.main()
