import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
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
        return self.driver.find_elements_by_id(id_)

    def find_element_by_name(self, name):
        try:
            elm = self.driver.find_element_by_name(name)
        except NoSuchElementException:
            elm = None
        return elm

    def find_elements_by_name(self, name):
        return self.driver.find_elements_by_name(name)

    def find_element_by_xpath(self, xpath):
        try:
            elm = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            elm = None
        return elm

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    @staticmethod
    def click(elm: WebElement, _sleep=1):
        time.sleep(_sleep)
        elm.click()
        time.sleep(_sleep)
