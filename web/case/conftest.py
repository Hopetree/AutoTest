import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 设置全局变量的原因是因为pytest_runtest_makereport方法中要用到
driver = None


@allure.title('给测试用例添加driver参数')
@pytest.fixture(scope='session')
def browser(config):
    global driver
    chrome_driver_path = config['executable_path']['chrome']  # 从环境配置中读取谷歌浏览器插件路径
    with allure.step('给测试类初始化driver对象'):
        driver = webdriver.Chrome(service=Service(chrome_driver_path))
    yield driver
    with allure.step('关闭浏览器'):
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    钩子函数，检查每个用例的执行结果，可以对失败的用例截图
    :param item:
    :param call:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        result_png = driver.get_screenshot_as_png()
        allure.attach(result_png, "失败用例截图", allure.attachment_type.PNG)
