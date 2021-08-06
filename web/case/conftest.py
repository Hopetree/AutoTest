import allure
import pytest
from selenium import webdriver


@allure.title('给测试类添加driver属性')
@pytest.fixture(scope='class')
def chrome_driver_init(request):
    driver = webdriver.Chrome('/Users/leizhu/Documents/Mac/chrome_extensions/chromedriver')
    request.cls.driver = driver
    yield
    driver.quit()
