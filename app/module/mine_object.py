from selenium.webdriver.common.by import By
from app.module.base_object import BasePage


class MinePage(BasePage):
    mine_id = 'com.meelive.ingkee:id/c50'

    def go_to_mine(self):
        self.find_element_by_id(self.mine_id).click()
