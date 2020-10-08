from page_appium.appium_base_page import AppiumBasePage
from page_appium.market import Market


class Main(AppiumBasePage):
    def goto_market(self):
        self.steps("../page_appium/main.yaml")
        return Market(self._driver)