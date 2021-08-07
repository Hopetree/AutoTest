import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from common.logger import logger


class BasePage:

    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, timeout)

    # 访问URL
    def get(self, url):
        self.driver.get(url)
        logger.debug(f'访问{url}')

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

    def back(self):
        """网页后退"""
        self.driver.back()
        logger.debug('网页后退')

    def forward(self):
        """网页前进"""
        self.driver.forward()
        logger.debug('网页前进')

    def refresh(self):
        """网页刷新"""
        self.driver.refresh()
        logger.debug('网页刷新')

    def get_current_url(self):
        """获取当前页面的URL"""
        return self.driver.current_url

    # 关闭
    def close(self):
        """关闭当前页面"""
        if self.driver:
            self.driver.close()
        logger.debug(f'关闭当前页面')

    def quite(self):
        """关闭所有页面，退出浏览器"""
        if self.driver:
            self.driver.quit()
        logger.debug('退出浏览器')
