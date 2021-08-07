import allure
import pytest


@allure.epic('pytest用法')
@allure.feature('mark模块')
@allure.story('测试自定义mark用法')
@pytest.mark.smoke
def test_mark():
    assert 1 == 1
