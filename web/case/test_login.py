import pytest
import allure
from selenium import webdriver

from web.module.logino_bject import LoginPage


@allure.story('登录页面')
class TestLoginPage:
    driver = webdriver.Chrome('/Users/leizhu/Documents/Mac/chrome_extensions/chromedriver')

    @pytest.fixture(scope='class')
    def close_driver(self):
        yield
        with allure.step('测试类结束，关闭浏览器'):
            self.driver.close()

    @pytest.mark.parametrize('username, password', [('user01', 'password'), ('admin', 'password')])
    @allure.title('测试多组账号密码登录')
    def test_login(self, close_driver, username, password):
        LoginPage(self.driver).login(username, password)
