import allure

from app.module.friend_object import FriendPage


@allure.story('交友页面')
class TestFriendPage:

    @allure.title('进入交友页面')
    def test_goto_friend(self, driver):
        FriendPage(driver).goto_friend()
        FriendPage(driver).close_dialog()
