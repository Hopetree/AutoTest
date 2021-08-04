import allure

from app.module.mine_object import MinePage


@allure.story('我的页面')
class TestMinePage:

    @allure.title('进入等级页面')
    def test_goto_level(self, driver):
        MinePage(driver).goto_mine()
        MinePage(driver).goto_level()
