from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_id(self, id_):
        try:
            elm = self.driver.find_element_by_id(id_)
        except NoSuchElementException:
            elm = None
        return elm

    def find_elements_by_id(self, id_):
        try:
            elms = self.driver.find_elements_by_id(id_)
        except NoSuchElementException:
            elms = None
        return elms
