import pytest
import allure


@allure.step(" ---- setup_module 整个.py文件开始时执行一次 ----- ")
def setup_module():
    pass


@allure.step(" ---- teardown_module 整个.py文件结束时执行一次 ----- ")
def teardown_module():
    pass


class TestFunc:
    @allure.step(" ---- setup_method 每个用例的setup前执行一次 ----- ")
    def setup_method(self, method):
        pass

    @allure.step(" ---- teardown_method 每个用例的teardown后执行一次 ----- ")
    def teardown_method(self, method):
        pass

    @classmethod
    def setup_class(cls):
        print(" ---- setup class 每个测试类开始前执行一次 ----- ")

    @classmethod
    def teardown_class(cls):
        print(" ---- teardown class 每个测试类结束后执行一次 ----- ")

    @allure.step(" ---- setUp 每个测试用例前执行一次 ----- ")
    def setup(self):
        pass

    @allure.step(" ---- teardown 每个测试用例后执行一次 ----- ")
    def teardown(self):
        pass

    def test_001(self):
        assert 1 == 2

    def test_002(self):
        assert 1 == 1


if __name__ == "__main__":
    pytest.main(["-s"])
