import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, timeout)

    # 访问URL
    def get(self, url):
        self.driver.get(url)

    # 元素定位
    def find_element(self, loc, is_wait=False):
        if is_wait:
            return self.waiter.until(ec.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

    def find_elements(self, loc, is_wait=False):
        if is_wait:
            return self.waiter.until(ec.presence_of_all_elements_located(loc))
        return self.driver.find_elements(*loc)

    # 输入
    def input(self, loc, txt, is_wait=False):
        elm = self.find_element(loc, is_wait)
        elm.clear()
        elm.send_keys(txt)

    # 点击
    def click(self, loc, is_wait=False):
        self.find_element(loc, is_wait).click()

    # 等待
    @staticmethod
    def wait(t):
        time.sleep(t)

    # 关闭
    def quite(self):
        self.driver.quit()

    def close(self):
        self.driver.close()
