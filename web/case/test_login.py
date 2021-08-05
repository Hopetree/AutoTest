import allure
import pytest

from common.readdata import YamlData
from web.module.logino_bject import LoginPage

user_data = YamlData('data/user.yaml').parametrize_data


@allure.story('登录页面')
class TestLoginPage:

    @pytest.mark.parametrize(*user_data)
    @allure.title('测试多组账号密码登录')
    def test_login(self, driver, username, password, code):
        LoginPage(driver).login(username, password)
        assert ('login' in driver.current_url) == code
