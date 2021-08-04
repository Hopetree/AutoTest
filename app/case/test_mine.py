import allure

from app.module.mine_object import MinePage


@allure.story('进入主页')
class TestMinePage:

    @allure.title('进入主页成功')
    def test_goto_mine(self, driver):
        MinePage(driver).go_to_mine()
