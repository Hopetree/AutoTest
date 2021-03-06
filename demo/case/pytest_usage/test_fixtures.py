import pytest
import allure

lis = []


@pytest.fixture(scope='module')
def func_module():
    with allure.step(" ---- scope=module 每个.py文件开始前执行一次 ----- "):
        lis.append('module start')
    yield lis
    with allure.step(" ---- scope=module 每个.py文件结束后执行一次 ----- "):
        lis.append('module end')


@pytest.fixture(scope='class')
def func_class(func_module):
    with allure.step(" ---- scope=class 每个测试类开始前执行一次 ----- "):
        func_module.append('class start')
    yield
    with allure.step(" ---- scope=class 每个测试类结束后执行一次 ----- "):
        func_module.append('class end')


@pytest.fixture()
def func_function(func_module):
    with allure.step(" ---- scope=function 每个函数开始前执行一次 ----- "):
        func_module.append('func start')
    yield
    with allure.step(" ---- scope=function 每个函数结束后执行一次 ----- "):
        func_module.append('func end')


@allure.epic('pytest用法')
@allure.feature('fixtures模块')
@allure.story('测试fixtures用法')
@allure.link('https://docs.pytest.org/en/latest/how-to/fixtures.html#yield-fixtures-recommended')
class TestCase:

    @allure.title('fixture 函数执行顺序')
    def test_01(self, func_function, func_class):
        assert lis == ['module start', 'class start', 'func start']

    @allure.title('fixture 函数执行顺序')
    def test_02(self, func_function, func_class):
        assert lis == ['module start', 'class start', 'func start', 'func end', 'func start']


if __name__ == '__main__':
    pytest.main([__file__])
