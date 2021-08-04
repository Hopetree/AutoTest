import pytest
import allure


@pytest.fixture(scope='class')
def config(conf):
    yield conf


lis = []


@allure.story('conftest用法')
class TestConftest:
    driver = None

    @pytest.fixture(scope='class', autouse=True)
    def set_config(self, config):
        """autouse属性为True，自动运行"""
        self.driver = 'driver'
        config['driver'] = 'driver'
        lis.append('set_config')

    def test_get_version(self, config):
        assert config['version'] == '0.1.0'

    @pytest.mark.xfail
    @allure.title('直接设置类属性不成功')
    @allure.description('设置类的属性不成功')
    def test_set_self(self):
        assert self.driver == 'driver'

    @allure.title('设置fixture属性成功')
    def test_set_config(self, config):
        assert config.get('driver') == 'driver'

    @allure.title('设置外部属性成功')
    def test_autouse(self):
        assert 'set_config' in lis
