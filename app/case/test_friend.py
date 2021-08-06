import pytest
import allure

from app.module.friend_object import FriendPage


@allure.story('交友页面')
@pytest.mark.usefixtures('driver_init')
class TestFriendPage:

    @allure.title('进入交友页面')
    def test_goto_friend(self):
        FriendPage(self.driver).goto_friend()
        FriendPage(self.driver).close_dialog()
