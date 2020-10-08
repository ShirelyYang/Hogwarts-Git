from page_appium.appium_base_page import AppiumBasePage
from page_appium.search import Search


class Market(AppiumBasePage):
    def goto_search(self):
        self.steps("../page_appium/market.yaml")
        return Search(self._driver)