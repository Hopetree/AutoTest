import pytest


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
