import allure
import pytest


@allure.title('模块属性conf')
@pytest.fixture(scope='module')
def conf():
    config = {
        "version": "0.1.0"
    }
    return config


@allure.title('给测试类添加默认属性name')
@pytest.fixture(scope="class")
def cls_init(request):
    request.cls.name = 'test'
    yield
