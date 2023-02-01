import allure
import pytest

from common.data_load import YamlData
from web.module.login_object import LoginPage

user_data = YamlData('data/user.yaml').parametrize_data


@allure.story('登录页面')
class TestLoginPage:

    @pytest.mark.parametrize(*user_data)
    @allure.title('多账号登录：{title}')
    def test_login(self, browser, username, password, code, title):
        driver = browser
        LoginPage(driver).login(username, password)
        # allure.attach(driver.get_screenshot_as_png(), "用例截图", allure.attachment_type.PNG)
        assert ('login' in driver.current_url) == code
