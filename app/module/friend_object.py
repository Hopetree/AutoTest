"""
    交友页面
"""
import time

import allure

from app.module.base_object import BasePage


class FriendPage(BasePage):
    # 主页-交友
    friend_id = 'com.meelive.ingkee:id/c52'
    # 主页-交友-【弹窗提示-确认】
    dialog_ok_id = 'com.meelive.ingkee:id/p4'

    @allure.step('从主页进入交友页面')
    def goto_friend(self):
        elm = self.find_element_by_id(self.friend_id)
        self.click(elm)

    @allure.step('关闭交友页面提示弹框')
    def close_dialog(self):
        dialog = self.find_element_by_id(self.dialog_ok_id)
        if dialog:
            self.click(dialog)
