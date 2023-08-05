# -*- coding: utf-8 -*-

from .service import PackageManagerConfig


class ConfigPack(object):
    def __init__(self, parsed_yaml):
        if parsed_yaml is None:
            parsed_yaml = {}

        # 全設定共有のテンプレート用変数
        self.environment = self.assign_dict(parsed_yaml, 'environment')
        self.services = []

        git = parsed_yaml.get('git', {})
        if git is not {}:
            git['environment'] = self.environment
            self.services.extend([PackageManagerConfig(git)])

        for service in parsed_yaml.get('services', []):
            if service is not None:
                self.services.extend([PackageManagerConfig(service)])

    @classmethod
    def assign_dict(cls, parsed_yaml: {}, key: str):
        configs = parsed_yaml.get(key, {})
        presets_configs = parsed_yaml.get('presets', {}).get(key, {})

        dictionary = {}
        for key in configs.keys():
            dictionary.setdefault(key, configs.get(key, ''))

        for key in presets_configs.keys():
            dictionary.setdefault(key, presets_configs.get(key, ''))

        return dictionary
