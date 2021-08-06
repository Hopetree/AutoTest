"""
    测试unit风格的函数执行顺序
"""
import pytest
import allure

lis = []


@allure.step(" ---- setup_module 整个.py文件开始时执行一次 ----- ")
def setup_module():
    lis.append('setup_module')


@allure.step(" ---- teardown_module 整个.py文件结束时执行一次 ----- ")
def teardown_module():
    lis.append('teardown_module')


@allure.story('测试xunit方法')
@allure.link('https://docs.pytest.org/en/latest/how-to/xunit_setup.html')
class TestCase:
    @allure.step(" ---- setup_method 每个用例的setup前执行一次 ----- ")
    def setup_method(self, method):
        lis.append('setup_method')

    @allure.step(" ---- teardown_method 每个用例的teardown后执行一次 ----- ")
    def teardown_method(self, method):
        lis.append('teardown_method')

    @classmethod
    def setup_class(cls):
        with allure.step(" ---- setup class 每个测试类开始前执行一次 ----- "):
            lis.append('setup_class')

    @classmethod
    def teardown_class(cls):
        with allure.step(" ---- teardown class 每个测试类结束后执行一次 ----- "):
            lis.append('teardown_class')

    @allure.step(" ---- setUp 每个测试用例前执行一次 ----- ")
    def setup(self):
        lis.append('setup')

    @allure.step(" ---- teardown 每个测试用例后执行一次 ----- ")
    def teardown(self):
        lis.append('teardown')

    @allure.title('xunit 函数执行顺序')
    def test_001(self):
        assert lis == ['setup_module', 'setup_class', 'setup_method', 'setup']


if __name__ == "__main__":
    pytest.main([__file__])
