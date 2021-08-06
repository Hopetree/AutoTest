import allure
import pytest


@pytest.fixture(scope="session")
def login_fixture():
    pass


@allure.step("步骤1")
def step_1():
    pass


@allure.step("步骤2")
def step_2():
    pass


@allure.step("步骤3")
def step_3():
    pass


@allure.epic('allure显示效果')
@allure.feature("feature模块")
class TestAllure:

    @allure.testcase("https://docs.qameta.io/allure/#_pytest", '点击跳转到测试用例地址')
    @allure.issue("https://docs.qameta.io/allure/#_pytest", '点击跳转到bug地址')
    @allure.title("用例的标题")
    @allure.story("多种显示效果")
    @allure.severity("critical")
    def test_case_1(self, login_fixture):
        """函数描述可以自动变成用例描述"""
        step_1()
        step_2()

    @allure.story("多种显示效果")
    @allure.description('用例描述-装饰器')
    def test_case_2(self, login_fixture):
        step_1()


@allure.epic('allure显示效果')
@allure.feature("feature模块")
class TestAllure2:
    @allure.story("story效果")
    def test_case_3(self, login_fixture):
        step_1()
        step_3()

    @allure.story("story效果")
    def test_case_4(self, login_fixture):
        step_3()

    @allure.title('用例title使用参数{name}')
    @allure.story("数据驱动支持")
    @pytest.mark.parametrize('name', ['allure'])
    def test_title_params(self, name):
        assert name == 'allure'
