import os
import pytest

if __name__ == '__main__':
    # 运行 pytest 并生产测试报告
    pytest.main(['--alluredir=./report', '--env=211', './app'])
    # 运行 allure 展示测试报告
    os.system('allure serve ./report')
