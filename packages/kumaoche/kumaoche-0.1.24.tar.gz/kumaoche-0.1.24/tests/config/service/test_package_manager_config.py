import unittest
from kumaoche.config import PackageManagerConfig


class TestPackageManagerConfig(unittest.TestCase):
    def test_init(self):
        parsed_yaml = {
            'lang': 'php',
            'env': 'docker',
            'php': {
                'run': '0',
                'setup': '1',
                'update': '2',
                'test': '3',
            },
            'node': {
                'run': '10',
                'setup': '11',
                'update': '12',
                'test': '13',
            }
        }

        config = PackageManagerConfig(parsed_yaml)
        self.assertEqual('0', config.run)
        self.assertEqual('1', config.setup)
        self.assertEqual('2', config.update)
        self.assertEqual('3', config.test)

        config = PackageManagerConfig({})
        self.assertEqual('', config.run)
        self.assertEqual('', config.setup)
        self.assertEqual('', config.update)
        self.assertEqual('', config.test)


if __name__ == '__main__':
    unittest.main()
