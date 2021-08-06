import pytest
import allure

from app.module.mine_object import MinePage


@allure.story('我的页面')
@pytest.mark.usefixtures('driver_init')
class TestMinePage:

    @allure.title('进入等级页面')
    def test_goto_level(self):
        MinePage(self.driver).goto_mine()
        MinePage(self.driver).goto_level()
