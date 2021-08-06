import os

import pytest
import allure


@pytest.fixture(scope='class')
def config(conf):
    yield conf


lis = []


@allure.epic('pytest用法')
@allure.feature('conftest模块')
@allure.story('conftest用法')
class TestConftest:
    driver = None

    @pytest.fixture(scope='class', autouse=True)
    def set_config(self, config):
        """autouse属性为True，自动运行"""
        self.driver = 'driver'
        config['driver'] = 'driver'
        lis.append('set_config')

    @allure.title('直接设置类属性不成功')
    @allure.description('设置类的属性不成功')
    @pytest.mark.xfail
    def test_set_self(self):
        assert self.driver == 'driver'

    @allure.title('设置fixture属性成功')
    def test_set_config(self, config):
        assert config.get('driver') == 'driver'

    @allure.title('设置外部属性成功')
    def test_autouse(self):
        assert 'set_config' in lis

    @allure.title('测试通过conftest设置环境变量')
    def test_get_env(self):
        assert os.getenv('env') == '211'


@allure.epic('pytest用法')
@allure.feature('conftest模块')
@allure.story('conftest用法')
@pytest.mark.usefixtures('cls_init')
class Test:
    @allure.title('usefixtures用法，给类添加属性')
    def test_usefixtures(self):
        assert self.name == 'test'
