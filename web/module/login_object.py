from selenium.webdriver.common.by import By

from web.module.base_object import BasePage


class LoginPage(BasePage):
    url = 'https://tendcode.com/accounts/login/'
    input_username = (By.NAME, 'login')
    input_password = (By.NAME, 'password')
    login_button = (By.XPATH, '//form[@class="login"]/button')

    def login(self, username, password):
        self.get(self.url)
        self.input(self.input_username, username, is_wait=True)
        self.input(self.input_password, password, is_wait=True)
        self.click(self.login_button, is_wait=True)
