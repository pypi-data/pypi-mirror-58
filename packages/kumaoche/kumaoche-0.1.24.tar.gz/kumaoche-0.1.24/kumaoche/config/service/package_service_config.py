# -*- coding: utf-8 -*-

from .service_config import ServiceConfig


class PackageManagerConfig(ServiceConfig):
    def __init__(self, configs: {}):
        super().__init__(configs)

        lang_config = configs.get(self.lang, {})
        self.test = configs.get('test', lang_config.get('test', ''))
