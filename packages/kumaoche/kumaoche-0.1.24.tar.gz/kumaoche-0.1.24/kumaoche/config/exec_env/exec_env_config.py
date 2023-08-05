# -*- coding: utf-8 -*-


class ExecEnvConfig(object):
    def __init__(self, parsed_yaml: {}, key: str):
        configs = parsed_yaml.get(key, {})

        self.working_dir = configs.get('working_dir', '')
        self.run = configs.get('run', '')
        self.build = configs.get('build', '')
        self.up = configs.get('up', '')
        self.down = configs.get('down', '')
