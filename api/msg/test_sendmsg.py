import unittest
import pytest
import allure


class TestMsg(unittest.TestCase):
    link = 'https://tendcode.com'

    @allure.step('发送信息')
    def sendmsg(self):
        self.step_1()
        self.step_2()
        self.step_3()

    @allure.step('1')
    def step_1(self):
        pass

    @allure.step('1')
    def step_2(self):
        pass

    @allure.step('1')
    def step_3(self):
        pass

    @allure.title('测试消息')
    def test_get(self):
        self.sendmsg()
        assert 1 == 1

    @allure.link(link)
    def test_link(self):
        assert 1 == 1
