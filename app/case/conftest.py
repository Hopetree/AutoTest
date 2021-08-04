import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def des_caps():
    caps = {
        'platformName': 'Android',
        # adb shell getprop ro.build.version.release
        'platformVersion': '5.1.1',  # 填写android虚拟机的系统版本
        # adb devices
        'deviceName': 'emulator-5554',  # 填写安卓虚拟机的设备名称
        # adb shell "dumpsys activity|grep mFocusedActivity"
        'appPackage': 'com.meelive.ingkee',  # 填写被测试包名
        'appActivity': '.business.main.entry.legacy.MainActivity',  # 填写被测试app入口
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    return caps


@pytest.fixture(scope='class')
def driver(des_caps):
    driver = webdriver.Remote('http://192.168.31.13:4723/wd/hub', des_caps)
    # 设置查找元素的超时时间
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
