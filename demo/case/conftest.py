import allure
import pytest


@allure.title('给测试类添加默认属性name')
@pytest.fixture(scope="class")
def cls_init(request):
    request.cls.name = 'test'
    yield
