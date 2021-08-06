import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome('/Users/leizhu/Documents/Mac/chrome_extensions/chromedriver')
    yield driver
    driver.quit()
