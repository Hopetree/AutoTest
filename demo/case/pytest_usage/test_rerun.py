import allure
import pytest


@allure.feature('pytest插件')
@allure.story('reruns重试')
@allure.title('设置了xfail的用例失败不会重试')
@pytest.mark.xfail
def test_rerun_01():
    assert 1 == 0


@allure.feature('pytest插件')
@allure.story('reruns重试')
@allure.title('报错重试')
def test_rerun_02():
    assert 1 == 0
