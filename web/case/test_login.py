import allure
import pytest

from common.read_data import YamlData
from web.module.login_object import LoginPage

user_data = YamlData('data/user.yaml').parametrize_data


@allure.story('登录页面')
@pytest.mark.usefixtures('chrome_driver_init')
class TestLoginPage:

    @pytest.mark.parametrize(*user_data)
    @allure.title('测试多组账号密码登录')
    def test_login(self, username, password, code):
        LoginPage(self.driver).login(username, password)
        assert ('login' in self.driver.current_url) == code
