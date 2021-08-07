import time

import allure
import pytest
from appium import webdriver
from selenium.common import exceptions

from common.logger import logger


@pytest.fixture(scope='session')
def des_caps():
    caps = {
        'platformName': 'Android',
        # adb shell getprop ro.build.version.release
        'platformVersion': '5.1.1',  # 填写android虚拟机的系统版本
        # adb devices
        'deviceName': 'emulator-5554',  # 填写安卓虚拟机的设备名称
        # adb shell "dumpsys activity|grep mFocusedActivity"
        # 'appPackage': 'com.meelive.ingkee',  # 填写被测试包名
        # 'appActivity': '.business.main.entry.legacy.MainActivity',  # 填写被测试app入口
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    return caps


@allure.title('给测试类添加driver属性')
@pytest.fixture(scope='class')
def driver_init(request, des_caps, config):
    with allure.step('连接appium'):
        driver = webdriver.Remote('http://192.168.31.13:4723/wd/hub', des_caps)
        # 设置查找元素的超时时间
        driver.implicitly_wait(10)
        with allure.step('打开APP,仅针对使用点击的APP需要'):
            app_name = config.get('app_name')
            driver.find_element_by_accessibility_id(app_name).click()
        request.cls.driver = driver
    yield
    time.sleep(5)
    with allure.step('关闭当前APP'):
        app_package = config.get('appPackage')
        try:
            driver.terminate_app(app_package, timeout=10000)
        except exceptions.WebDriverException:
            logger.warning('使用appPackage关闭APP失败，忽略')
        # driver.close_app()
    with allure.step('关闭appium连接'):
        driver.quit()
