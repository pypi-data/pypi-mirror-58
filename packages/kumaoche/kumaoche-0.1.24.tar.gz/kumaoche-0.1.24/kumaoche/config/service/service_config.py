# -*- coding: utf-8 -*-

from ..exec_env import ShellConfig, DockerConfig, StringBuilderConfig


class ServiceConfig(object):
    def __init__(self, configs: {}):

        self.lang = configs.get('lang', '')
        self.env = configs.get('env', '')
        self.environment = configs.get('environment', '')
        self.string_builder = StringBuilderConfig(configs, 'string_builder')
        self.shell = ShellConfig(configs, 'shell')
        self.docker = DockerConfig(configs, 'docker')

        # service 毎の各言語用コマンドは個別設定を優先する
        lang_config = configs.get(self.lang, {})
        self.run = configs.get('run', lang_config.get('run', ''))
        self.setup = configs.get('setup', lang_config.get('setup', ''))
        self.update = configs.get('update', lang_config.get('update', ''))
