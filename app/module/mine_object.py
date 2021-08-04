"""
    我的页面
"""
import allure

from app.module.base_object import BasePage


class MinePage(BasePage):
    # 主页-我的
    mine_id = 'com.meelive.ingkee:id/c50'
    # 主页-我的-等级
    level_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'

    @allure.step('从主页进入我的页面')
    def goto_mine(self):
        elm = self.find_element_by_id(self.mine_id)
        self.click(elm)

    @allure.step('从我的页面进入等级页面')
    def goto_level(self):
        elm = self.find_element_by_xpath(self.level_xpath)
        self.click(elm)
