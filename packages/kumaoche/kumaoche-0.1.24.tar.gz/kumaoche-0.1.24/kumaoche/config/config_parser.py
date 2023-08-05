# -*- coding: utf-8 -*-

import yaml
import os
import sys

from .config_pack import ConfigPack


class ConfigParser(object):

    @classmethod
    def file_path_list(cls):
        return os.environ.get('KUMAOCHE_CONFIG_PATH', os.getcwd() + '/kumaoche_config.yml').split(':')

    @classmethod
    def all_repository_names(cls, file_path_list=None):
        loaded_yaml = cls.yaml_load(file_path_list)
        loaded_repository_keys = list(loaded_yaml.get('repositories', {}).keys())

        # 順序を維持した重複削除
        return sorted(set(loaded_repository_keys), key=loaded_repository_keys.index)

    @classmethod
    def find(cls, repo: str, file_path_list=None):
        loaded_yaml = cls.yaml_load(file_path_list)
        parsed_yaml = cls.parse_version(loaded_yaml)
        loaded_repository = cls.find_repository_config(parsed_yaml, repo)

        return ConfigPack(loaded_repository)

    @classmethod
    def yaml_load(cls, file_path_list=None):
        if file_path_list is None:
            file_path_list = cls.file_path_list()

        # ファイル存在確認
        for path in file_path_list:
            if not os.path.exists(path):
                print(f'Target config file "{path}" is not exist.')
                sys.exit()

        loaded_yaml = {
            'presets': {
                "environment": {
                    'git_host': 'github.com',
                    'git_org': '',
                    'git_repo': '',
                },
                "shell": {
                    'working_dir': '`ghq root`/{git_host}/{git_org}/{git_repo}',
                    'run': '{command}',
                    'build': '',
                    'up': '',
                    'down': '',
                },
                "docker": {
                    'container_name': '',
                    'working_dir': '`ghq root`/{git_host}/{git_org}/{git_repo}',
                    'run': 'docker-compose run --rm {container} /bin/bash -c "{command}"',
                    'build': 'docker-compose build',
                    'up': 'docker-compose up -d',
                    'down': 'docker-compose down',
                },
                "git": {
                    'lang': 'git',
                    'env': 'shell',
                    'run': '{command}',
                    'setup': 'ghq get git@{git_host}:{git_org}/{git_repo}.git',
                    'update': 'ghq get git@{git_host}:{git_org}/{git_repo}.git && cd `ghq root`/{git_host}/{git_org}/{git_repo} && git switch master && git pull',
                    'test': '',
                    "shell": {
                        'working_dir': '',
                        'run': '{command}',
                        'build': '',
                        'up': '',
                        'down': '',
                    },
                },
                "php": {
                    'run': '{command}',
                    'setup': 'php -d detect_unicode=Off composer.phar install',
                    'update': 'php -d detect_unicode=Off composer.phar install',
                    'test': './vendor/bin/phpunit',
                },
                "ruby": {
                    'run': '{command}',
                    'setup': 'bundle install --path vendor/bundle',
                    'update': 'bundle install --path vendor/bundle',
                    'test': 'bundle exec rspec --color',
                },
                "node": {
                    'run': '{command}',
                    'setup': 'npm install',
                    'update': 'npm install',
                    'test': 'npm test',
                },
            }
        }

        for file_path in file_path_list:
            with open(file_path) as file:
                new_yaml = yaml.safe_load(file)
                presets = loaded_yaml.get('presets', {})
                loaded_presets = new_yaml.get('presets', {})
                new_presets = {
                    "environment": {**presets.get("environment", {}), **loaded_presets.get("environment", {})},
                    "shell": {**presets.get("shell", {}), **loaded_presets.get("shell", {})},
                    "docker": {**presets.get("docker", {}), **loaded_presets.get("docker", {})},
                    "git": {**presets.get("git", {}), **loaded_presets.get("git", {})},
                    "php": {**presets.get("php", {}), **loaded_presets.get("php", {})},
                    "ruby": {**presets.get("ruby", {}), **loaded_presets.get("ruby", {})},
                    "node": {**presets.get("node", {}), **loaded_presets.get("node", {})},
                }
                loaded_yaml = {**loaded_yaml, **new_yaml, **{'presets': new_presets}}

        return loaded_yaml

    @classmethod
    def parse_version(cls, loaded_yaml):
        version = int(loaded_yaml.get('version', 1))

        if version == 1:
            return loaded_yaml
        else:
            print(f'Yaml version "{version}" is invalid.')
            sys.exit()

    @classmethod
    def find_repository_config(cls, loaded_yaml, repo):
        # 指定リポジトリが設定ファイルに存在するか確認
        loaded_repositories = loaded_yaml.get('repositories', {})
        if repo not in list(loaded_repositories.keys()):
            print(f'Target repository "{repo}" is not exist.')
            sys.exit()

        loaded_repository = loaded_repositories.get(repo, {})

        presets = loaded_yaml.get('presets', {})
        result = {
            "environment": {**presets.get("environment", {}), **cls.safe_get_hash(loaded_repository, "environment")},
            "shell": {**presets.get("shell", {}), **cls.safe_get_hash(loaded_repository, "shell")},
            "docker": {**presets.get("docker", {}), **cls.safe_get_hash(loaded_repository, "docker")},
            "git": {**presets.get("git", {}), **cls.safe_get_hash(loaded_repository, "git")},
            "php": {**presets.get("php", {}), **cls.safe_get_hash(loaded_repository, "php")},
            "ruby": {**presets.get("ruby", {}), **cls.safe_get_hash(loaded_repository, "ruby")},
            "node": {**presets.get("node", {}), **cls.safe_get_hash(loaded_repository, "node")},
            "services": [],
        }

        # 抽出対象に git リポジトリを上書き
        result['environment']['git_repo'] = repo

        for service in cls.safe_get_array(loaded_repository, "services"):
            if service is None:
                continue

            result['services'].extend([{
                "lang": service.get("lang", ""),
                "env": service.get("env", ""),
                "environment": {**result.get("environment", {}), **cls.safe_get_hash(service, "environment")},
                "shell": {**result.get("shell", {}), **cls.safe_get_hash(service, "shell")},
                "docker": {**result.get("docker", {}), **cls.safe_get_hash(service, "docker")},
                "git": {**result.get("git", {}), **cls.safe_get_hash(service, "git")},
                "php": {**result.get("php", {}), **cls.safe_get_hash(service, "php")},
                "ruby": {**result.get("ruby", {}), **cls.safe_get_hash(service, "ruby")},
                "node": {**result.get("node", {}), **cls.safe_get_hash(service, "node")},
            }])

        return result

    @classmethod
    def safe_get_hash(cls, dictionary: {}, key: str):
        if dictionary is None:
            dictionary = {}

        result = dictionary.get(key, {})
        if result is None:
            result = {}

        return result

    @classmethod
    def safe_get_array(cls, dictionary: {}, key: str):
        if dictionary is None:
            dictionary = {}

        result = dictionary.get(key, [])
        if result is None:
            result = []

        return result
