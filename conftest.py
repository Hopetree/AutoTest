"""
这个文件是所有用例执行的前置操作，做的事情如下：
1. 添加命令行参数
2. 将命令行参数写入环境变量
3. 将环境变量写入到allure的环境变量文件中
"""
import os

import allure
import pytest

from common.config_load import ConfigYaml
from settings import BASE_DIR


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default='dev',
        type=str,
        help="assign which env to use",
    )


@allure.title('设置环境变量')
@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    # 定义一个字典，按照键值对写入环境变量中，只需要在这里追加要设置的环境变量即可
    env_option_kv = {
        'env': '--env',
    }
    # 将环境变量写入到报告到环境变量配置中，便于查看
    allure_dir = request.config.getoption('--alluredir')
    allure_env_file = os.path.join(BASE_DIR, allure_dir, 'environment.properties')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        for _k, _v in env_option_kv.items():
            value = request.config.getoption(_v)
            f.write(f'{_k}={value}')
            # 将命令行传参写入环境变量中，方便用例调用
            os.environ[_k] = value


@allure.title('根据传入的env环境参数设置配置信息config')
@pytest.fixture(scope='session')
def config(request):
    _env = request.config.getoption('--env')
    _config = ConfigYaml(_env).get_config()
    yield _config
