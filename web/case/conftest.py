import allure
import pytest
from selenium import webdriver


@allure.title('给测试类添加driver属性')
@pytest.fixture(scope='class')
def chrome_driver_init(request):
    with allure.step('给测试类初始化driver对象'):
        driver = webdriver.Chrome('/Users/leizhu/Documents/Mac/chrome_extensions/chromedriver')
        request.cls.driver = driver
    yield
    with allure.step('关闭浏览器'):
        driver.quit()
