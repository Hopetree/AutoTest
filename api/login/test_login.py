import allure
from common.read_config import Config

config = Config()


@allure.tag('我是tag')
def test_004():
    assert config.name == 111


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
