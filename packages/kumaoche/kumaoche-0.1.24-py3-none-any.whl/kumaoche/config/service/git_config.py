# -*- coding: utf-8 -*-

from .service_config import ServiceConfig


class GitConfig(ServiceConfig):
    def __init__(self, configs: {}):
        configs = {**configs, **{'lang': 'git', 'env': 'shell'}}

        super().__init__(configs)

        lang_config = configs.get(self.lang, {})
        self.repo_dir = configs.get('repo_dir', lang_config.get('repo_dir', ''))
