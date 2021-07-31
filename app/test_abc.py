import pytest
import allure

data = [(0, 0, True), (1, 1, True), (1, True, True), (0, False, True)]


@pytest.mark.parametrize('a,b,code', data)
def test_eq(a, b, code):
    if code is True:
        story = '成功'
    else:
        story = '失败'
    allure.dynamic.story(story)
    allure.dynamic.title(f'测试{a}与{b}是否相等')
    assert (a == b) == code
