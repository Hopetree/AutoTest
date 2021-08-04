import allure
import pytest
from appium import webdriver

from app.module.mine_object import MinePage


@pytest.fixture(scope='class')
def driver(des_caps):
    driver = webdriver.Remote('http://192.168.31.13:4723/wd/hub', des_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.story('进入主页')
class TestMinePage:

    @allure.title('进入主页成功')
    def test_goto_mine(self, driver):
        MinePage(driver).go_to_mine()
