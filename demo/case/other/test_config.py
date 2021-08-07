import os

import allure

from common.logger import logger


@allure.epic('pytest用法')
@allure.feature('conftest模块')
@allure.story('config用法')
class TestConfig:

    def test_001(self, config):
        assert config.get('name') is not None
