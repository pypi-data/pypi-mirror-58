import unittest
from kumaoche.config import StringBuilderConfig


class TestStringBuilderConfig(unittest.TestCase):
    def test_init(self):
        parsed_yaml = {
            'string_builder': {
                'run': '0',
                'name': '1',
                'working_dir': '2',
                'build': '5',
                'up': '6',
                'down': '7',
            }
        }
        config = StringBuilderConfig(parsed_yaml, 'string_builder')
        self.assertEqual('0', config.run)
        self.assertEqual('2', config.working_dir)
        self.assertEqual('5', config.build)
        self.assertEqual('6', config.up)
        self.assertEqual('7', config.down)

        config = StringBuilderConfig({}, 'string_builder')
        self.assertEqual('', config.run)
        self.assertEqual('', config.working_dir)
        self.assertEqual('', config.build)
        self.assertEqual('', config.up)
        self.assertEqual('', config.down)


if __name__ == '__main__':
    unittest.main()
