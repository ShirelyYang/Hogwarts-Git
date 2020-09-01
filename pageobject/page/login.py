from selenium.webdriver.common.by import By

from base_page import BasePage
from register import Register


class Login(BasePage):
    def scan(self):
        pass

    def register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)